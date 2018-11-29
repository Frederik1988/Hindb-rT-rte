import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import sys, termios, tty, os, time
import socket

TCP_IP = "192.168.24.239"
TCP_PORT = 9576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((TCP_IP, TCP_PORT)) 

messageLocked = "The door is locked"

messageUnlocked = "The door is unlocked"

messageNightTime = "The lock has automatically been locked. It is still possible to unlock the door"

messageQuit = "Goodbye.."

sense = SenseHat()

g = (0,255,0)
r = (0,0,0)
s = (255,0,0)

locked = [
r,s,s,s,s,s,s,r, 
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,r,s,r,r,s,r,r,  
r,r,s,r,r,s,r,r, 
r,r,r,s,s,r,r,r,    
r,r,r,r,r,r,r,r,
]

unlocked = [
r,g,g,g,g,g,g,r,
r,g,g,g,g,g,g,r,
r,g,g,g,g,g,g,r,
r,g,g,g,g,g,g,r,
r,r,r,r,r,g,r,r,
r,r,g,r,r,g,r,r,
r,r,r,g,g,r,r,r,
r,r,r,r,r,r,r,r,
]

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)
sense.set_pixels(unlocked)


while True:
  
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        pwm.ChangeDutyCycle(12)
        sense.set_pixels(unlocked)
      elif event.direction == "down":
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(locked)
  
  data = sock.recv(1024)
  message = data.decode('utf-8')
  message = message [0: -2]
 
  
  if (message =='l'):
    pwm.ChangeDutyCycle(7)
    sense.set_pixels(locked)
    sock.send(bytes(messageLocked, "UTF-8"))
  if (message == 'o'):
    pwm.ChangeDutyCycle(12)
    sense.set_pixels(unlocked)
    sock.send(bytes(messageUnlocked, "UTF-8"))
  if (message == 'q'):
    sock.send(bytes(messageQuit, "UTF-8"))
    break
   
  if (message == 'n'):
    sense.set_pixels(locked)
    sock.send(bytes(messageNightTime, "UTF-8"))
  
   
  for event in sense.stick.get_events():
    if event.action == "pressed":
      if event.direction == "up":
        pwm.ChangeDutyCycle(12)
        sense.set_pixels(unlocked)
      elif event.direction == "down":
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(locked)
  
