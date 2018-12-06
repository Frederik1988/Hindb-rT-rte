import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import socket
import asyncio


TCP_IP = "192.168.24.239"
TCP_PORT = 9576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((TCP_IP, TCP_PORT)) 

messageLocked = "The door is locked"

messageUnlocked = "The door is unlocked"

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
s = (0,0,0)

locked = [
s,r,r,r,r,r,r,s, 
s,r,r,r,r,r,r,s,
s,r,r,r,r,r,r,s,
s,r,r,r,r,r,r,s,
s,s,r,s,s,r,s,s,  
s,s,r,s,s,r,s,s, 
s,s,s,r,r,s,s,s,    
s,s,s,s,s,s,s,s,
]

unlocked = [
s,g,g,g,g,g,g,s,
s,g,g,g,g,g,g,s,
s,g,g,g,g,g,g,s,
s,g,g,g,g,g,g,s,
s,s,s,s,s,g,s,s,
s,s,g,s,s,g,s,s,
s,s,s,g,g,s,s,s,
s,s,s,s,s,s,s,s,
]

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(7)
sense.set_pixels(locked)
i=0

async def recieveMessage():
  
  while True:
    
    data = sock.recv(1024)
    message = data.decode('utf-8')
    message = message [0: -2]
    await message
  
    if (message =='l'):
      pwm.ChangeDutyCycle(7)
      sense.set_pixels(locked)
      sock.send(bytes(messageLocked, "UTF-8"))
      i = 1   

    if (message == 'o'):    
      pwm.ChangeDutyCycle(12)
      sense.set_pixels(unlocked)
      sock.send(bytes(messageUnlocked, "UTF-8"))
      i = 0
  


async def joystick(i):
  
  if (i==0):
    for event in sense.stick.get_events():
      if event.action == "pressed":
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(locked)
        i = 1
        
  if (i==1):
    for event in sense.stick.get_events():
      if event.action == "pressed":
        pwm.ChangeDutyCycle(12)
        sense.set_pixels(unlocked)
        i = 0
  
loop = asyncio.get_event_loop() 
cors = asyncio.wait([recieveMessage(),joystick(i)])
loop.run_until_complete(cors)
