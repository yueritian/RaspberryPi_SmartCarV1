###################################################
#               智能小车1.0 -- 超声波传感器模块
#
#               @author chenph
#               @date 2018/5/10
###################################################

import RPi.GPIO as GPIO
import time


class UltrasonicSensor:
    ECHO_TIMEOUT_SECONDS = 0.05

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
        wait_started = time.monotonic()
        while GPIO.input(self.PIN_ECHO) == 0:
            if time.monotonic() - wait_started > self.ECHO_TIMEOUT_SECONDS:
                return None
        pulse_start = time.monotonic()

        # 等待高电平结束，然后记录时间。
        while GPIO.input(self.PIN_ECHO) == 1:
            if time.monotonic() - pulse_start > self.ECHO_TIMEOUT_SECONDS:
                return None
        pulse_end = time.monotonic()

        pulse_duration = pulse_end - pulse_start
        # distance = pulse_duration * 17150
        distance = pulse_duration * 340 / 2
        return round(distance, 2)


if __name__ == "__main__":
    try:
        m = UltrasonicSensor(11, 13)
        print(m.getDistance())
    except KeyboardInterrupt:
        pass
    GPIO.cleanup()
