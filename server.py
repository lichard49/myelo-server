from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi import Request
from fastapi.templating import Jinja2Templates

import time
import os


templates = Jinja2Templates(directory='templates')
app = FastAPI()

connected_output_sockets = []

recording = False
record_file = None


@app.get('/')
async def home(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})


@app.get('/webserial')
async def webserial(request: Request):
	return templates.TemplateResponse('webserial.html', {'request': request})


@app.get('/record')
async def record(request: Request):
  global recording, record_file

  recording_request = request.query_params['recording']

  if recording_request == 'true':
    record_file_name = time.strftime('%Y_%m_%d-%H_%M_%S',
      time.localtime(time.time()))
    record_file_path = os.path.join('data', record_file_name + '.csv')
    record_file = open(record_file_path, 'w')
    recording = True
    return 1
  elif recording_request == 'false':
    recording = False
    record_file.close()
    return 0

  return -1


@app.websocket('/sockets/output')
async def output_socket(websocket: WebSocket):
  await websocket.accept()
  connected_output_sockets.append(websocket)

  try:
    while True:
      await websocket.receive_text()
  except WebSocketDisconnect:
    connected_output_sockets.remove(websocket)


@app.websocket('/sockets/input')
async def input_socket(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()

    if recording:
      record_file.write(data + '\n')

    for output_socket in connected_output_sockets:
      await output_socket.send_text(data)
