import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)


while True:
  
  pwm.start(18)
  time.sleep(3)
  pwm.ChangeDutyCycle(2)
  time.sleep(3)
