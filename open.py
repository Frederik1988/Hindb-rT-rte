from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

r = (0,255,0)
g = (255,0,0)
s = (0,0,0)

  
locked = [
r,r,r,r,r,r,r,r,
r,r,r,s,s,r,r,r,
r,r,s,r,r,s,r,r,
r,r,r,r,r,r,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
r,s,s,s,s,s,s,r,
]

while True:
  sense.set_pixels(locked)
