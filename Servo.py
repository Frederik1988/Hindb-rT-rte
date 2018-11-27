import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)


while True:
  
  pwm.start(30)
  time.sleep(3)
  pwm.ChangeDutyCycle(90)
  time.sleep(3)
