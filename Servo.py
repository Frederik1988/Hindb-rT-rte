import RPi.GPIO as GPIO
import time
from sense_hat import SenseHat
import sys, termios, tty, os, time

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
s = (0,0,0)

def getch():
    fd = sys.stdin.fileno()
    old_settings = termios.tcgetattr(fd)
    try:
        tty.setraw(sys.stdin.fileno())
        ch = sys.stdin.read(1)
 
    finally:
        termios.tcsetattr(fd, termios.TCSADRAIN, old_settings)
    return ch
 
button_delay = 0.2

locked = [
r,r,r,r,r,r,r,r,
r,r,r,s,s,r,r,r,
r,r,s,r,r,s,r,r,
r,s,r,r,r,r,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
]

open = [
g,g,g,g,g,g,g,g,
g,g,g,s,s,g,g,g,
g,g,s,g,g,s,g,g,
g,g,g,g,g,g,s,g,
g,s,s,s,s,s,s,g,
g,s,s,s,s,s,s,g,
g,s,s,s,s,s,s,g,
g,s,s,s,s,s,s,g,
]

    
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)

while True:
 char = getch()
 if (char =='l'):
  pwm.ChangeDutyCycle(7)
  sense.set_pixels(locked)
 if (char == 'o'):
  pwm.ChangeDutyCycle(12)
  sense.set_pixels(open)
 
 if (char == 'q'):
  break
 
    

