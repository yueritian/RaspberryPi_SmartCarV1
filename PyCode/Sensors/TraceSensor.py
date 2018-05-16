###################################################
#               智能小车1.0 -- 寻迹传感器模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class TraceSensor:
    # 静态变量
    TRACE_SENSOR_ONWAY = 0
    TRACE_SENSOR_OUTWAY = 1

    # 初始化传感器
    def __init__(self, PIN):
        print('Infrared Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(PIN, GPIO.IN)

    # 获取状态
    # 0 在路上
    # 1 偏航
    def getStatus(self):
        return GPIO.input(self.PIN)
