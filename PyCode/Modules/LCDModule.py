###################################################
#               智能小车1.0 -- LCD1602液晶屏
#
#               @author chenph
#               @date 2018/5/19
###################################################

import smbus2
from time import sleep


def delay(time):
    sleep(time / 1000.0)


def delayMicroseconds(time):
    sleep(time / 1000000.0)


class Screen():
    enable_mask = 1 << 2
    rw_mask = 1 << 1
    rs_mask = 1 << 0
    backlight_mask = 1 << 3

    data_mask = 0x00

    def __init__(self, cols=16, rows=2, addr=0x3f, bus=1):
        self.cols = cols
        self.rows = rows
        self.bus_num = bus
        self.bus = smbus2.SMBus(self.bus_num)
        self.addr = addr
        self.display_init()

    def enable_backlight(self):
        self.data_mask = self.data_mask | self.backlight_mask

    def disable_backlight(self):
        self.data_mask = self.data_mask & ~self.backlight_mask

    def warning(self):

            self.disable_backlight()
            sleep(1)
            self.enable_backlight()
            sleep(1)

    def display_data(self, *args):
        self.clear()
        for line, arg in enumerate(args):
            self.cursorTo(line, 0)
            self.println(arg[:self.cols].ljust(self.cols))

    def cursorTo(self, row, col):
        offsets = [0x00, 0x40, 0x14, 0x54]
        self.command(0x80 | (offsets[row] + col))

    def clear(self):
        self.command(0x10)

    def println(self, line):
        for char in line:
            self.print_char(char)

    def print_char(self, char):
        char_code = ord(char)
        self.send(char_code, self.rs_mask)

    def display_init(self):
        delay(1.0)
        self.write4bits(0x30)
        delay(4.5)
        self.write4bits(0x30)
        delay(4.5)
        self.write4bits(0x30)
        delay(0.15)
        self.write4bits(0x20)
        self.command(0x20 | 0x08)
        self.command(0x04 | 0x08, delay=80.0)
        self.clear()
        self.command(0x04 | 0x02)
        delay(3)

    def command(self, value, delay=50.0):
        self.send(value, 0)
        delayMicroseconds(delay)

    def send(self, data, mode):
        self.write4bits((data & 0xF0) | mode)
        self.write4bits((data << 4) | mode)

    def write4bits(self, value):
        value = value & ~self.enable_mask
        self.expanderWrite(value)
        self.expanderWrite(value | self.enable_mask)
        self.expanderWrite(value)

    def expanderWrite(self, data):
        self.bus.write_byte_data(self.addr, 0, data | self.data_mask)


if __name__ == "__main__":
    try:
        screen = Screen(bus=1, addr=0x3f, cols=16, rows=2)
        line = "01234567890123456789"
        screen.enable_backlight()
        while True:
            screen.display_data(line, line[::-1])
            sleep(1)
            screen.display_data(line[::-1], line)
            sleep(1)
    except KeyboardInterrupt:
        pass
