from sense_hat import SenseHat
from random import randint
import time

sense = SenseHat()

count = 0.1
t = 0.5

def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  

  
while (t>0.3):
  o = pick_random_colour()
  
  all_pixels = [
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o,
  o,o,o,o,o,o,o,o
]
  sense.set_pixels(all_pixels)
  time.sleep(t)
  t = t-count
  if (t>0.2):
    t += 0.1
  sense.clear()
  
