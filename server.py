from fastapi import FastAPI
from fastapi import WebSocket
from fastapi import Request
from fastapi.templating import Jinja2Templates


templates = Jinja2Templates(directory='templates')
app = FastAPI()


@app.get('/')
async def home(request: Request):
	return templates.TemplateResponse('index.html', {'request': request})


@app.websocket('/websocket_endpoint')
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    print('Message text was:', data)
