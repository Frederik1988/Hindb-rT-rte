import RPi.GPIO as GPIO
import time
import socket

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(("192.168.24.12", 9576)) 

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

s.close()
