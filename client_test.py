import asyncio
from websockets import connect

import random
import math


def getRandomNumbers(i):
  return ','.join([str(random.randint(0, 1024)) for _ in range(i)])


def getSineWave(i, j):
  return ','.join([str(math.sin(j * 0.2) * (k + 1) * j) for k in range(i)])


async def sendRandomNumbers(uri, n=1000, i=3, fs=10):
  period = 1/fs
  async with connect(uri) as websocket:
    for j in range(n):
      # data = getRandomNumbers(i)
      data = getSineWave(i, j)
      await websocket.send(data)
      await asyncio.sleep(period)


asyncio.run(sendRandomNumbers('ws://127.0.0.1:8000/sockets/input'))
