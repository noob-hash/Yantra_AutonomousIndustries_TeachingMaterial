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

def backward():
 all_motor_off()
 motor_on(10)
 motor_on(11)

def right():
 all_motor_off()
 motor_on(8)

def left():
 all_motor_off()
 motor_on(12)

def main():
 all_motor_off()
 sleep(2)
 forward()
 sleep(2)
 all_motor_off()

if __name__ == "__main__":
 main()