from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
app = FastAPI()

connected_output_sockets = []

@app.get('/')
async def home(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})


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
    for output_socket in connected_output_sockets:
      await output_socket.send_text(data)
