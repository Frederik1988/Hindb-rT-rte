import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

GPIO.setup(12, GPIO.OUT)

p = GPIO.PWM(12, 50)

p.start(7.5)

counter = 0

try:
    while True:
        p.ChangeDutyCycle(7.5)  # 90 grader
        time.sleep(1) 
        p.ChangeDutyCycle(2.5)  # 0 grader
        time.sleep(1) 
        p.ChangeDutyCycle(12.5) # 180 grader
        time.sleep(1) 
        
        counter = counter+1
        
        if(counter==5):
          p.stop()
          GPIO.cleanup()
            
except KeyboardInterrupt:
    print("CTRL-C: Terminating program.")
finally:
    print("Cleaning up GPIO...")
    GPIO.cleanup()
