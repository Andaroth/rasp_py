import RPi.GPIO as GPIO
import time

# serigraphie
GPIO.setmode(GPIO.BOARD)

# config les E/S
GPIO.setup(3, GPIO.OUT, initial = 1)

# easy blink
while True:
    GPIO.output(3, not GPIO.input(3))
    time.sleep(0.5)