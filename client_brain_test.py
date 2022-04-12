import asyncio
from websockets import connect

import random
import math
import time
from threading import Thread
from queue import Queue

import numpy as np

from brainflow_interfacing import HeadSet, File

# def queue_data(q, input_source):
#   while True:
#     from_ring = input_source.board.get_board_data()[1:9]
#     if len(from_ring[0]) >= 1:
#       print(np.shape(from_ring))
#       print('conditional more than one sample')
#       for sample in np.transpose(from_ring):
#         q.put(sample)

# def pull_data(q):
#   if not q.empty():
#     sample = q.get()
#   else:
#     return None
#   data = ",".join(str(s) for s in sample) + '\n'
#   print('pulled')
#   return data

# async def sendBrainData(uri):
#   async with connect(uri) as websocket:
#     num = 0
#     # for n in range(30000):
#     while True:
#       data = None
#       while data is None:
#         data = pull_data(q)
#       print('final data', data)
#       print(num)
#       num += 1
#       await websocket.send(data)


async def sendBrainData(uri, sr):
  async with connect(uri) as websocket:
    while True:
      batch = input_source.board.get_board_data()[1:9]
      for sample in np.transpose(batch):
        data = ",".join(str(s) for s in sample) + '\n'
        print(data)
        await websocket.send(data)
        time.sleep(1/sr)

input_source = File("eeg-alpha-1.csv")

# q = Queue()

# start streaming here
input_source.init_board()
input_source.start_session()

# queue_brain_data = Thread(target=queue_data, args=(q, input_source))

# queue_brain_data.start()

asyncio.run(sendBrainData('ws://127.0.0.1:8000/sockets/input', 250))

# def pull_data(input_source):
#   data = input_source.board.get_board_data()[1:9]
#   while len(data[0]) == 0:
#     data = input_source.board.get_board_data()[1:9]
#   print('data is not empty', np.shape(data))
#   return str(data.flatten())
#   # get current board data (256) would pull the latest, but not remove from buffer