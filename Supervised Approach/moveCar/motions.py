import RPi.GPIO as gpio
import time

def init():
        gpio.setmode(gpio.BOARD)
        gpio.setup(16, gpio.OUT)
        gpio.setup(18, gpio.OUT)
        gpio.setup(13, gpio.OUT)
        gpio.setup(15, gpio.OUT)

def forward(tf):
        init()
        print "forward"
        gpio.output(16,True)
        gpio.output(18, False)
        gpio.output(13, True)
        gpio.output(15, True)
        time.sleep(tf)
        gpio.cleanup()

def left(tf):
        init()
        print "left"
        gpio.output(16, True)
        gpio.output(18, True)
        gpio.output(13, True)
        gpio.output(15, False)
        time.sleep(tf)
        gpio.cleanup()

def right(tf):
        init()
        print "right"
        gpio.output(16, True)
        gpio.output(18, True)
        gpio.output(13, False)
        gpio.output(15, True)
        time.sleep(tf)
        gpio.cleanup()

def takeAction(action=None):
        if(action == 'forward'):
                forward(0.8)
        elif(action == 'left'):
                left(0.3)
                forward(0.5)
                right(0.1)
        elif(action == 'right'):
                right(0.3)
                forward(0.5)
                left(0.1)       
        else:
                print "No action is being specified"
