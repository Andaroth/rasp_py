import RPi.GPIO as gp
import time
gp.cleanup()

# serigraphie
gp.setmode(gp.BOARD)

# config les E/S
gp.setup(3, gp.OUT, initial = 1)

# easy blink
while True:
    gp.output(3, not gp.input(3))
    time.sleep(0.5)