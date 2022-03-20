PIN_YELLOW_BUTTON=38 # GPIO 20
PIN_BLUE_BUTTON=40 # GPIO 21
PIN_YELLOW_LED=16 # GPIO 23
PIN_BLUE_LED=18 # GPIO 24

from common import Color, IoInterface
import time
import RPi.GPIO as GPIO 

class IoGPIO(IoInterface):
    def __init__(self):
        GPIO.setmode(GPIO.BOARD) # Use physical pin numbering
        GPIO.setup(PIN_YELLOW_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(PIN_BLUE_BUTTON, GPIO.IN, pull_up_down=GPIO.PUD_DOWN)
        GPIO.setup(PIN_YELLOW_LED, GPIO.OUT)
        GPIO.setup(PIN_BLUE_LED, GPIO.OUT)
        self.led(Color.BLUE,False)
        self.led(Color.BLUE,False)
        time.sleep(0.2)
        self.led(Color.BLUE,True)
        time.sleep(0.2)
        self.led(Color.BLUE,False)
        time.sleep(0.2)
        self.led(Color.YELLOW,True)
        time.sleep(0.2)
        self.led(Color.YELLOW,False)
    
    def led(self, color,on):
        if color == Color.YELLOW:
            pin = PIN_YELLOW_LED
        else:
            pin = PIN_BLUE_LED

        if on:
            GPIO.output(pin,GPIO.HIGH)
        else:
            GPIO.output(pin,GPIO.LOW)
    
    def pressed(self, color):
        if color == Color.YELLOW:
            pin = PIN_YELLOW_BUTTON
        else:
            pin = PIN_BLUE_BUTTON
        return GPIO.input(pin) == GPIO.HIGH


