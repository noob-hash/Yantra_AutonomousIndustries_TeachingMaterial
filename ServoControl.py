import RPi.GPIO as GPIO
from time import sleep

def setup_servo(pins):
 servo = []
 for pin in pins:
  GPIO.setup(pin,GPIO.OUT)
  pwm = GPIO.PWM(pin,50)
  pwm.start(0)
  servo.append(pwm)
 return servo

def cleanup(servos):
 for servo in servos:
  servo.stop()
 GPIO.cleanup()

def set_angle(servo,angle):
 duty_cycle = 2 + (angle/18)
 servo.ChangeDutyCycle(duty_cycle)
 sleep(0.5)

def reset_servo(servos):
 for servo in servos:
  servo.ChangeDutyCycle(2+(90/18))
  sleep(0.5)

def catch():
 pin = [38,40,5]

 GPIO.setmode(GPIO.BOARD)
 servos = setup_servo(pin)

 set_angle(servos[0],125)
 set_angle(servos[1],55)
 set_angle(servos[2],55)

def release():
 pin = [38,40,5]

 GPIO.setmode(GPIO.BOARD)
 servos = setup_servo(pin)

 reset_servo(servos)
 cleanup(servos)

def cam_back():
 pin = [7]

 GPIO.setmode(GPIO.BOARD)
 servos = setup_servo(pin)

 set_angle(servos[0],0)
 cleanup(servos)

def cam_front():
 pin = [7]

 GPIO.setmode(GPIO.BOARD)
 servos = setup_servo(pin)

 set_angle(servos[0],180)
 cleanup(servos)

def main():
 catch()
 sleep(1)
 cam_back()
 sleep(1)
 release()
 sleep(1)
 cam_front()

if __name__=="__main__":
 main()