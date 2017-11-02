#!/usr/bin/python
import RPi.GPIO as gp
import time

count = 0

# serigraphie
gp.setmode(gp.BOARD)

# config les E/S
gp.setup(3, gp.OUT, initial = 1)

# easy blink
while True:
    count+=1;
    print("Run : " + count + ". pin 3 is on " + gp.input(3));
    gp.output(3, not gp.input(3))
    time.sleep(0.5)