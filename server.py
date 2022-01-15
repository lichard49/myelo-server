from fastapi import FastAPI, WebSocket


app = FastAPI()


@app.websocket('/websocket_endpoint')
async def websocket_endpoint(websocket: WebSocket):
  await websocket.accept()
  while True:
    data = await websocket.receive_text()
    print('Message text was:', data)
