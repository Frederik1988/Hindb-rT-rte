from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
s = (0,0,0)

  
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
while True:
  sense.set_pixels(locked)
  time.sleep(3)
  sense.set_pixels(open)
  time.sleep(3)
  
  
  
