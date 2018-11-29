from sense_hat import SenseHat
from time import sleep
sense = SenseHat()
import RPi.GPIO as GPIO

sense = SenseHat()

g = (0,255,0)
r = (0,0,0)
s = (255,0,0)

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

GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)
sense.set_pixels(unlocked)

while True:
  
  if (sense.set_pixels(locked) == True):
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      if event.direction == "middle":
        pwm.ChangeDutyCycle(7)
        sense.set_pixels(locked)
   
   if (sense.set_pixels(locked) == True):
    for event in sense.stick.get_events():
    # Check if the joystick was pressed
    if event.action == "pressed":
      if event.direction == "middle":
        pwm.ChangeDutyCycle(12)
        sense.set_pixels(unlocked)
  
  
        

        
  

  
