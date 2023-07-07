import RPi.GPIO as GPIO
from time import sleep

class ExoskeletonControl():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        self.pwm1 = GPIO.PWM(11,50)
        self.pwm1.start(0)
        sleep(1)
        GPIO.setup(13,GPIO.OUT)
        self.pwm2 = GPIO.PWM(13,50)
        self.pwm2.start(0)
        
    def SetAngle(self, angle,servo):
        duty = angle / 18 + 2
        if servo == 0:
            GPIO.output(11, True)
            self.pwm1.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(11, False)
            self.pwm1.ChangeDutyCycle(0)
        if servo == 1:
            GPIO.output(13, True)
            self.pwm2.ChangeDutyCycle(duty)
            sleep(1)
            GPIO.output(13, False)
            self.pwm2.ChangeDutyCycle(0)
        else:
            print("select a servo to change duty cycle")

    # def give_feedback(self):
    #     GPIO.output(13, True)
    #     sleep(0.5)
    #     GPIO.output(13, False)

