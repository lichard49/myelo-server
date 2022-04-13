import asyncio
from websockets import connect

import serial
import time
import sys


async def sendUsbData(uri):
  if len(sys.argv) < 2:
    print('Usage: python client_usb.py <SERIAL_PORT>')
    sys.exit(0)
  serial_port = sys.argv[1]

  usb_device = serial.Serial(serial_port, 115200)
  async with connect(uri) as websocket:
    while True:
      data = usb_device.readline().decode('utf-8')
      print(time.time(), data)
      await websocket.send(data)
      await asyncio.sleep(0.0001)


asyncio.run(sendUsbData('ws://127.0.0.1:8000/sockets/input'))
