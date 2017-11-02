import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# getmode
configuration = GPIO.getmode()
print("conf: "+configuration)

# config les E/S
GPIO.setup(3, GPIO.OUT)
GPIO.setup(9, GPIO.IN)

state = GPIO.gpio_function(pin)
print(state)

p = GPIO.PWM(3, 1) # PWM sur 3, fréquence haute
p.start(50)
p.ChangeFrequency(0) # fréquence basse (off)
p.ChangeDutCycle(50)
p.stop

GPIO.cleanup()