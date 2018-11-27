import RPi.GPIO as GPIO
import time
import socket

host = '192.168.24.239'
port = 9576

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

print(s)

s.connect((host,port))

data = s.recv(1024)
    
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
