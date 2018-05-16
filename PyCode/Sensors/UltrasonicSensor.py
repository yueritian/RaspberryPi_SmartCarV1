###################################################
#               智能小车1.0 -- 超声波传感器模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class UltrasonicSensor:
    # 静态变量
    LIGHT_SENSOR_LIGHT = 0
    LIGHT_SENSOR_DARK = 1

    # 初始化传感器
    def __init__(self, PIN_TRIG, PIN_ECHO):
        print('Ultrasonic Sensor In Progress')
        GPIO.setmode(GPIO.BOARD)
        self.PIN_TRIG = PIN_TRIG
        self.PIN_ECHO = PIN_ECHO
        GPIO.setup(self.PIN_TRIG, GPIO.OUT)
        GPIO.setup(self.PIN_ECHO, GPIO.IN)

    # 获取距离 单位m
    def getDistance(self):
        # 发送 trig 信号  持续 15us 的方波脉冲
        # 高电平
        GPIO.output(self.PIN_TRIG, GPIO.HIGH)
        time.sleep(0.000015)
        # 低电平
        GPIO.output(self.PIN_TRIG, GPIO.LOW)

        # 等待低电平结束，然后记录时间。
        while GPIO.input(self.PIN_ECHO) == 0:
            pass
        pulse_start = time.time()

        # 等待高电平结束，然后记录时间。
        while GPIO.input(self.PIN_ECHO) == 1:
            pass
        pulse_end = time.time()

        pulse_duration = pulse_end - pulse_start
        # distance = pulse_duration * 17150
        distance = pulse_duration * 340 / 2
        return round(distance, 2)

