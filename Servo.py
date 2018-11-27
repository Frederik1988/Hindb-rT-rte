import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(29, GPIO.OUT)

p = GPIO.PWM(29, 50)

p.start(7.5)

p.ChangeDutyCycle(7.5)  # 90 grader
