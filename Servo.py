import RPi.GPIO as GPIO
import time
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)

if (input("L"):
    pvm.ChangeDutyCycle(12)
 
if (input("O"):
    pwm.ChangeDutyCycle(7)
    

