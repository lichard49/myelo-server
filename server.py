from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import WebSocketDisconnect
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
app = FastAPI()

connected_visualization_sockets = []

@app.get('/')
async def home(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})


@app.websocket('/visualization_socket')
async def visualization_socket(websocket: WebSocket):
  await websocket.accept()
  connected_visualization_sockets.append(websocket)

  try:
    while True:
      await websocket.receive_text()
  except WebSocketDisconnect:
    connected_visualization_sockets.remove(websocket)


@app.websocket('/websocket_endpoint')
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    for visualization_socket in connected_visualization_sockets:
      await visualization_socket.send_text(data)
