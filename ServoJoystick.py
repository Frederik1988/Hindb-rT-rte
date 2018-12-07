import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import socket
from multiprocessing import Process
from threading import Thread

TCP_IP = "192.168.1.233"
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


def joystick(i): 
  if (i == 0):
    for event in sense.stick.get_events():
      if event.action == "pressed":
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(locked)
        i = 1
        
  if (i == 1):
    for event in sense.stick.get_events():
      if event.action == "pressed":
        pwm.ChangeDutyCycle(12)
        sense.set_pixels(unlocked)
        i = 0

def recieveMessage():
  
  data = sock.recv(1024)
  message = data.decode('utf-8')
  message = message [0: -2]
      
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

        
if __name__ = "__main__":
	i = 1
	
thread1 = threading.Thread(target=recieveMessage)
thread2 = threadig.Thread(target=joystick, args=(i,)
			  
thread1.start()
thread2.start()

thread1.join()
thread2.join()
