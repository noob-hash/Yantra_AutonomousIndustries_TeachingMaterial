import RPi.GPIO as GPIO
from time import sleep,time

def distance1():
    GPIO.setmode(GPIO.BOARD)
    trigger1 = 36
    echo1 = 37


    GPIO.setup(trigger1,GPIO.OUT)
    GPIO.setup(echo1,GPIO.IN)

    GPIO.output(trigger1,False)
    sleep(0.1)
    GPIO.output(trigger1,True)
    sleep(0.00001)
    GPIO.output(trigger1,False)

    startTime = time()
    stopTime = time()

    while GPIO.input(echo1) == 0:
        startTime = time()

    while GPIO.input(echo1) == 1:
        stopTime = time()

    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 17510)
    distance = round(distance,2)
    return abs(distance)

def distance2():
    GPIO.setmode(GPIO.BOARD)
    trigger2 = 35
    echo2 = 33

    GPIO.setup(trigger2,GPIO.OUT)
    GPIO.setup(echo2,GPIO.IN)

    GPIO.output(trigger2,False)
    sleep(0.1)
    GPIO.output(trigger2,True)
    sleep(0.00001)
    GPIO.output(trigger2,False)

    startTime = time()
    stopTime = time()

    while GPIO.input(echo2) == 0:
        startTime = time()

    while GPIO.input(echo2) == 1:
        stopTime = time()

    timeElapsed = stopTime - startTime
    distance = (timeElapsed * 17510)
    distance = round(distance,2)
    return abs(distance)


if __name__ == "__main__":
    while True:
        print("1:",distance1())
        print("2:",distance2())

