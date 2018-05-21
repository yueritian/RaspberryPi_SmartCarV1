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
    TRACE_SENSOR_ONWAY = 1
    TRACE_SENSOR_OUTWAY = 0

    # 初始化传感器
    def __init__(self, PIN):
        print('Infrared Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(PIN, GPIO.IN)

    # 获取状态
    # 0 偏航
    # 1 在路上
    def getStatus(self):
        return GPIO.input(self.PIN)


if __name__ == "__main__":
    try:
        m = TraceSensor(35)
        print(m.getStatus())
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()