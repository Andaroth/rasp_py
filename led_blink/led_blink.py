import RPi.GPIO as GPIO
GPIO.setmode(GPIO.BOARD)

# getmode
configuration = GPIO.getmode()
print("conf: "+configuration)

# setting the I/O
GPIO.setup(3, GPIO.OUT)
GPIO.setup(9, GPIO.IN)

state = GPIO.gpio_function(pin)
print(state)

GPIO.cleanup()