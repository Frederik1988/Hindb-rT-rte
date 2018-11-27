import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(3, GPIO.OUT)

p = GPIO.PWM(3, 50)

p.start(7.5)

time.sleep(2)

p.ChangeDutyCycle(2.5)  # 90 grader
