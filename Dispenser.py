import RPi.GPIO as GPIO
import time
from Pill_Info import pillinfo

class Dispenser():
    def __init__(self, id, servoPIN) -> None:
        GPIO.setmode(GPIO.BCM)
        GPIO.setup(servoPIN, GPIO.OUT)
        self.dispenser = pillinfo(id)
        self.pwm = GPIO.PWM(servoPIN, 50)
        self.pwm.start(12.5) # Initialization

    def dispense(self):
        self.pwm.ChangeDutyCycle(2.5)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(12.5)
        time.sleep(1)
        self.pwm.ChangeDutyCycle(0)