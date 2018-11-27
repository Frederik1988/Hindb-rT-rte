import RPi.GPIO as GPIO
import time
import socket

TCP_IP = '1127.0.0.1' 
TCP_PORT = 9576
BUFFER_SIZE = 1024

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect((TCP_IP, TCP_PORT))

data = s.recv(BUFFER_SIZE)
    
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)

while True:
 
 if (data =='l'):
  pwm.ChangeDutyCycle(7)
 if (data == 'o'):
  pwm.ChangeDutyCycle(12)
 
 if (char == 'q'):
  break
