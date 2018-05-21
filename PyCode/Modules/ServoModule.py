###################################################
#               智能小车1.0 -- 舵机模块
#
#               @author chenph
#               @date 2018/5/15
###################################################

import RPi.GPIO as GPIO
import time


class ServoModule:

    # 初始模块
    def __init__(self, PIN):
        print('Servo Module In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(self.PIN, GPIO.OUT, initial=GPIO.LOW)

        self.pwm = GPIO.PWM(self.PIN, 50)
        self.pwm.start(0)
        self.pwm.ChangeDutyCycle(6.5)

    # 左转
    def turnLeft(self):
        self.pwm.ChangeDutyCycle(2.5)
        time.sleep(0.02)
        self.pwm.ChangeDutyCycle(0)

    # 右转
    def turnRight(self):
        self.pwm.ChangeDutyCycle(12.5)
        time.sleep(0.02)
        self.pwm.ChangeDutyCycle(0)


if __name__ == "__main__":
    try:
        # 19,21,23
        m = ServoModule(19)
        m.turnLeft()
        time.sleep(5)
        m.turnRight()
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()