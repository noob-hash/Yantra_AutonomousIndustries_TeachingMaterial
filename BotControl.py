import RPi.GPIO as GPIO
from time import sleep
GPIO.setmode(GPIO.BOARD)

pins = [8,10,11,12]

for pin in pins:
 GPIO.setup(pin,GPIO.OUT)

def motor_on(pin):
 GPIO.output(pin,GPIO.LOW)

def motor_off(pin):
 GPIO.output(pin,GPIO.HIGH)

def all_motor_off():
 GPIO.setmode(GPIO.BOARD)

 pins = [8,10,11,12]

 for pin in pins:
  GPIO.setup(pin,GPIO.OUT)

 for pin in pins:
  motor_off(pin)

def forward():
 all_motor_off()
 motor_on(8)
 motor_on(12)
 sleep(0.25)
 all_motor_off()

def backward():
 all_motor_off()
 motor_on(10)
 motor_on(11)
 sleep(0.25)
 all_motor_off()

def right():
 all_motor_off()
 motor_on(11)
 motor_on(8)
 sleep(0.25)
 all_motor_off()

def left():
 all_motor_off()
 motor_on(10)
 motor_on(12)
 sleep(0.25)
 all_motor_off()

def main():
 all_motor_off()
 sleep(0.25)
 forward()
 sleep(0.25)
 backward()
 sleep(0.25)
 left()
 sleep(0.25)
 right()
 sleep(0.25)
 all_motor_off()

if __name__ == "__main__":
 main()