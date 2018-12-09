import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import socket
import threading

TCP_IP = "192.168.1.233"
TCP_PORT = 9576

sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

sock.connect((TCP_IP, TCP_PORT)) 

messageLocked = "The door is locked"

messageUnlocked = "The door is unlocked"

messageJoystickUnlock = "The door is unlocked by joystick"

messageJoystickLock = "The door is locked by joystick"

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
s = (0,0,0)

locked = [
  s,s,s,s,s,s,s,s,
  s,s,s,r,r,s,s,s,
  s,s,r,s,s,r,s,s,
  s,s,r,s,s,r,s,s,  
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s,
  s,r,r,r,r,r,r,s
]

unlocked = [
  s,s,s,s,s,s,s,s,
  s,s,s,g,g,s,s,s,
  s,s,g,s,s,g,s,s,
  s,s,s,s,s,g,s,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s,
  s,g,g,g,g,g,g,s
]

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(7)
sense.set_pixels(locked)

def joystick(i): 
  
  while True:
    
    if (i ==1):
      
      for event in sense.stick.get_events():
        if event.action == "pressed":
          pwm.ChangeDutyCycle(12)
          sock.send(bytes(messageJoystickUnlock, "UTF-8"))
          sense.show_message(str("HA EN DEJLIG DAG"), scroll_speed=0.05, text_colour=[0, 0, 255])
          sense.set_pixels(unlocked)
          i = 0
    
    if (i == 0):
      for event in sense.stick.get_events():
        if event.action == "pressed":
          pwm.ChangeDutyCycle(7)
          sock.send(bytes(messageJoystickLock, "UTF-8"))
          sense.set_pixels(locked)
          i = 1
          

def recieveMessage(i):
  
  while True:    
  
    data = sock.recv(1024)
    fromServer = data.decode('utf-8')
    message =  fromServer [0 : 1 -len(fromServer)]
    name = fromServer [1 : len(fromServer)-2]
  
          
    if (message =='l'):
    
      pwm.ChangeDutyCycle(7)
      sense.set_pixels(locked)
      sock.send(bytes(messageLocked, "UTF-8"))
      i = 1
      
    if (message == 'o'):  
      
      pwm.ChangeDutyCycle(12)        
      sock.send(bytes(messageUnlocked, "UTF-8"))
      sense.show_message(str("VELKOMMEN HJEM " + name), scroll_speed=0.05, text_colour=[0, 0, 255])
      i = 0
      sense.set_pixels(unlocked)
      
      
if __name__ == "__main__":
	i = 1

thread1 = threading.Thread(target=recieveMessage, args=(i,))
thread2 = threading.Thread(target=joystick, args=(i,))
			  
thread1.start()
thread2.start()

thread1.join()
thread2.join()
