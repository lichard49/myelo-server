import asyncio
from websockets import connect

import random


async def sendRandomNumbers(uri, n=1000, i=3, fs=10):
  period = 1/fs
  async with connect(uri) as websocket:
    for _ in range(n):
      data = ','.join([str(random.randint(0, 1024)) for _ in range(i)])
      await websocket.send(data)
      await asyncio.sleep(period)


asyncio.run(sendRandomNumbers('ws://127.0.0.1:8000/sockets/input'))
