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

# step is just some value I choose to make bot slower
# you can have your own preferred one or even not use sleep
  
def forward(step = 25):
 all_motor_off()
 motor_on(8)
 motor_on(12)
 sleep(step/100)
 all_motor_off()

def backward(step = 25):
 all_motor_off()
 motor_on(10)
 motor_on(11)
 sleep(step/100)
 all_motor_off()

def right(step = 25):
 all_motor_off()
 motor_on(11)
 motor_on(8)
 sleep(step/100)
 all_motor_off()

def left(step = 25):
 all_motor_off()
 motor_on(10)
 motor_on(12)
 sleep(step/100)
 all_motor_off()

def main():
 all_motor_off()
 sleep(1)
 forward()
 sleep(1)
 backward()
 sleep(1)
 left()
 sleep(1)
 right()
 sleep(1)
 all_motor_off()

if __name__ == "__main__":
 main()