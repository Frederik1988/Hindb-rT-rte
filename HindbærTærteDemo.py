from sense_hat import SenseHat
from time import sleep
from random import randint

sense = SenseHat()

green = (0, 255, 0)
yellow = (255, 255, 0)
blue = (0, 0, 255)
red = (255, 0, 0)
white = (255,255,255)
nothing = (0,0,0)
pink = (255,105, 180)

def pick_random_colour():
  random_red = randint(0, 255)
  random_green = randint(0, 255)
  random_blue = randint(0, 255)
  return (random_red, random_green, random_blue)
  
sense.show_message("F", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("R", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("E", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("D", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("E", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("R", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("I", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
sense.show_message("K", text_colour=nothing, back_colour=pick_random_colour(), scroll_speed=0.03)
  

while True:
  t = sense.get_temperature()
  p = sense.get_pressure()
  h = sense.get_humidity()
  
  t = round(t, 1)
  p = round(p, 1)
  h = round(h, 1)
  
  if (h<45):
    sense.show_message("ET ER DEJLIGT BEDSTEFAR", text_colour=green, scroll_speed=0.05)
    
  else:
    sense.show_message("LUMMERHEDEN ER OVER OS", text_colour=red, scroll_speed=0.05)
  
  if (t>23):
    sense.show_message(",Puha, det er varmt!",text_colour=red, scroll_speed=0.05)
  
  else:
    sense.show_message("DET ER DET RENE GRØNLAND", text_colour=green, scroll_speed=0.05)
    
