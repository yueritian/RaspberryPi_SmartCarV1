###################################################
#               智能小车1.0 -- 无源蜂鸣传感器模块
#
#               @author chenph
#               @date 2018/5/15
###################################################

import RPi.GPIO as GPIO
import time


class BeeSensor:

    # 初始化传感器
    def __init__(self, PIN):
        print('Bee Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(self.PIN, GPIO.OUT, initial=GPIO.HIGH)

    def play(self, sleepTime=0.2):
        for i in range(5):
            GPIO.output(self.PIN, GPIO.LOW)
            time.sleep(sleepTime)
            GPIO.output(self.PIN, GPIO.HIGH)
            time.sleep(sleepTime)
