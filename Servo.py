import RPi.GPIO as GPIO
import time
import keyboard

    
GPIO.setmode (GPIO.BOARD)
GPIO.setup (11, GPIO.OUT)
pwm = GPIO.PWM (11, 50)
pwm.start(12)

while True:
    
    if keyboard.is_pressed('l')
        pvm.ChangeDutyCycle(12)
        
    if keyboard.is_pressed('o')
        pwm.ChangeDutyCycle(7)
    

