import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import sys, termios, tty, os, time
import socket

TCP_IP = "192.168.24.188"
TCP_PORT = 9576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((TCP_IP, TCP_PORT)) 

sense = SenseHat()

g = (0,0,255)
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
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,r,r,r,r,s,r,r,
r,r,s,r,r,s,r,r,
r,r,r,s,s,r,r,r,
r,r,r,r,r,r,r,r,
]

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)
sense.set_pixels(unlocked)


while True:
  data = sock.recv(1024)
  message = data.decode('utf-8')
  message = message [0: -2]
    
  print(message)
  
  if (message =='l'):
    pwm.ChangeDutyCycle(7)
    sense.set_pixels(locked)
  if (message == 'o'):
    pwm.ChangeDutyCycle(12)
    sense.set_pixels(unlocked)
  if (message == 'q'):
    break
  
