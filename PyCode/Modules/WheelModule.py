###################################################
#               智能小车1.0 -- 电机模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class WheelModule:

    # 初始化
    def __init__(self, PIN_IN1_L, PIN_IN2_L, PIN_IN1_R, PIN_IN2_R):
        print('Wheel Module In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN_IN1_L = PIN_IN1_L
        self.PIN_IN2_L = PIN_IN2_L
        self.PIN_IN1_R = PIN_IN1_R
        self.PIN_IN2_R = PIN_IN2_R
        GPIO.setup(self.PIN_IN1_L, GPIO.OUT)
        GPIO.setup(self.PIN_IN2_L, GPIO.OUT)
        GPIO.setup(self.PIN_IN1_R, GPIO.OUT)
        GPIO.setup(self.PIN_IN2_R, GPIO.OUT)

    # 前进的代码
    def forward(self):
        GPIO.output(self.PIN_IN1_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    # 后退
    def backOff(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN1_R, GPIO.LOW)
        GPIO.output(self.PIN_IN2_R, GPIO.HIGH)

    # 左转
    def leftTurn(self):
        GPIO.output(self.PIN_IN1_L, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.LOW)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    # 右转
    def rightTurn(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.HIGH)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)

    # 停止
    def stop(self):
        GPIO.output(self.PIN_IN1_L, GPIO.LOW)
        GPIO.output(self.PIN_IN2_L, GPIO.LOW)
        GPIO.output(self.PIN_IN1_R, GPIO.LOW)
        GPIO.output(self.PIN_IN2_R, GPIO.LOW)


if __name__ == "__main__":
    try:
        m = WheelModule(32, 36, 40, 38)
        m.forward()
        time.sleep(5)
        m.stop()
        time.sleep(1)

        m.backOff()
        time.sleep(5)
        m.stop()
        time.sleep(1)

        m.leftTurn()
        time.sleep(2)
        m.stop()
        time.sleep(1)

        m.rightTurn()
        time.sleep(2)
        m.stop()
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()