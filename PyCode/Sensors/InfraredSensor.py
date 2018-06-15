###################################################
#               智能小车1.0 -- 红外避障传感器模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class InfraredSensor:
    # 静态变量
    INFRARED_SENSOR_BLOCK = 0
    INFRARED_SENSOR_CLEAR = 1

    # 初始化传感器
    def __init__(self, PIN):
        print('Infrared Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN = PIN
        GPIO.setup(PIN, GPIO.IN)

    # 获取状态
    # 0 有障碍福
    # 1 无障碍福
    def getStatus(self):
        return GPIO.input(self.PIN)


if __name__ == "__main__":
    try:
        # 37,27
        m = InfraredSensor(37)
        print(m.getStatus())
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()