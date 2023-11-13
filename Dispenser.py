import RPi.GPIO as GPIO
import time

servoPIN = 13
GPIO.setmode(GPIO.BCM)
GPIO.setup(servoPIN, GPIO.OUT)

p = GPIO.PWM(servoPIN, 50) # GPIO 13 for PWM with 50Hz
p.start(12.5) # Initialization
try:
    while True:
        p.ChangeDutyCycle(0)
        user = input("Dispenser Pill?: (yes/no) ")
        if user == "yes":
            p.ChangeDutyCycle(2.5)
            time.sleep(1)
            p.ChangeDutyCycle(12.5)
            time.sleep(1)
        elif user == "no":
            pass
        else:
            print("Try Again")
except KeyboardInterrupt:
  p.stop()
  GPIO.cleanup()