import RPi.GPIO as GPIO
import time

GPIO.setmode(GPIO.BOARD)

# getmode
#configuration = GPIO.getmode()
#print("conf: "+configuration)

# config les E/S
GPIO.setup(3, GPIO.OUT, initial = 1)
#GPIO.setup(9, GPIO.IN)

#state = GPIO.gpio_function(pin)
#print(state)

"""
p = GPIO.PWM(3, 1) # PWM sur 3, fréquence haute
p.start(50)
p.ChangeFrequency(0) # fréquence basse (off)
p.ChangeDutCycle(50)
p.stop
"""

while True:
    GPIO.output(3, not GPIO.input(3))
    time.sleep(0.5)