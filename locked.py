from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

g = (0,255,0)
r = (255,0,0)
s = (0,0,0)
o = (255,127,80)
  
locked = [
r,r,r,r,r,r,r,r,
r,r,r,s,s,r,r,r,
r,r,s,r,r,s,r,r,
r,s,r,r,r,r,s,r,
r,o,o,o,o,o,o,r,
r,s,s,s,s,s,s,r,
r,s,s,r,r,s,s,r,
r,s,s,r,r,s,s,r,
]

while True:
  sense.set_pixels(locked)
