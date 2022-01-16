import asyncio
from websockets import connect

import random


async def sendRandomNumbers(uri, n=1000):
  async with connect(uri) as websocket:
    for _ in range(n):
      await websocket.send(str(random.randint(0, 1024)))
      await asyncio.sleep(0.1)


asyncio.run(sendRandomNumbers('ws://127.0.0.1:8000/websocket_endpoint'))
