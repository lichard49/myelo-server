import asyncio
from websockets import connect

import serial
import time


async def sendUsbData(uri):
  usb_device = serial.Serial('/dev/tty.usbmodem14101', 115200)
  async with connect(uri) as websocket:
    while True:
      data = usb_device.readline().decode('utf-8')
      print(time.time(), data)
      await websocket.send(data)
      await asyncio.sleep(0.0001)


asyncio.run(sendUsbData('ws://127.0.0.1:8000/sockets/input'))
