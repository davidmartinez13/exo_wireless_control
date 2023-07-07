import RPi.GPIO as GPIO
from time import sleep

class ExoskeletonControl():
    def __init__(self):
        GPIO.setmode(GPIO.BOARD)
        GPIO.setup(11,GPIO.OUT)
        GPIO.setup(13,GPIO.OUT)
        self.pwm1 = GPIO.PWM(11,50)
        self.pwm2 = GPIO.PWM(13,50)
        self.pwm1.start(0)
        self.pwm2.start(0)
        
    def SetAngle(self,angle1,angle2):
        # self.give_feedback()
        # thumb
        duty1 = angle1 / 18 + 2
        GPIO.output(11, True)
        self.pwm1.ChangeDutyCycle(duty1)
        sleep(0.5)
        GPIO.output(11, False)
        self.pwm1.ChangeDutyCycle(0)
        sleep(0.5)
        # index
        duty2 = angle2 / 18 + 2
        GPIO.output(13, True)
        self.pwm2.ChangeDutyCycle(duty2)
        sleep(0.5)
        GPIO.output(13, False)
        self.pwm2.ChangeDutyCycle(0)

    # def give_feedback(self):
    #     GPIO.output(13, True)
    #     sleep(0.5)
    #     GPIO.output(13, False)

