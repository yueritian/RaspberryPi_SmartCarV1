###################################################
#               智能小车1.0 -- 光敏传感器模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class LightSensor:
    # 静态变量
    LIGHT_SENSOR_LIGHT = 0
    LIGHT_SENSOR_DARK = 1

    # 初始化传感器
    def __init__(self, PIN):
        print('Light Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(PIN, GPIO.IN)

    # 获取状态
    # 0 身处光明
    # 1 身处黑暗
    def getStatus(self):
        return GPIO.input(self.PIN)
