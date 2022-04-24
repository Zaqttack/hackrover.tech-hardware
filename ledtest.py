import RPi.GPIO as GPIO
import time

#17,27,22,23,24


GPIO.setmode(GPIO.BCM)
GPIO.setwarnings(False)

GPIO.setup(17,GPIO.OUT)
GPIO.setup(27,GPIO.OUT)
GPIO.setup(22,GPIO.OUT)
GPIO.setup(23,GPIO.OUT)
GPIO.setup(24,GPIO.OUT)


def ledRout1():
    GPIO.output(17,GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(17,GPIO.LOW)
    time.sleep(.50)
    print(17)
    GPIO.output(27,GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(27,GPIO.LOW)
    time.sleep(.50)
    print(27)
    GPIO.output(22,GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(22,GPIO.LOW)
    time.sleep(.50)
    print(22)
    GPIO.output(23,GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(23,GPIO.LOW)
    time.sleep(.50)
    print(23)
    GPIO.output(24,GPIO.HIGH)
    time.sleep(.100)
    GPIO.output(24,GPIO.LOW)
    time.sleep(.50)
    print(24)

h = GPIO.HIGH
l = GPIO.LOW

def ledRout2():
    GPIO.output(17,h)
    GPIO.output(27,h)
    GPIO.output(22,h)
    GPIO.output(23,h)
    GPIO.output(24,h)
    time.sleep(0.5)
    GPIO.output(17,l)
    GPIO.output(27,l)
    GPIO.output(22,l)
    GPIO.output(23,l)
    GPIO.output(24,l)
    



ledRout1()
while(1):
    ledRout2()
    time.sleep(0.2)
