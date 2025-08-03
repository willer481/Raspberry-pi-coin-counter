from micropython import const
import framebuf

SET_CONTRAST = const(0x81)
SET_NORMAL_DISPLAY = const(0xA6)
DISPLAY_ON = const(0xAF)
DISPLAY_OFF = const(0xAE)
SET_DISPLAY_CLOCK_DIV = const(0xD5)
SET_MULTIPLEX = const(0xA8)
SET_DISPLAY_OFFSET = const(0xD3)
SET_START_LINE = const(0x40)
SET_CHARGE_PUMP = const(0x8D)
SET_SEGMENT_REMAP = const(0xA1)
SET_COM_SCAN_DEC = const(0xC8)
SET_COM_PINS = const(0xDA)
SET_PRECHARGE = const(0xD9)
SET_VCOM_DETECT = const(0xDB)
SET_MEMORY_MODE = const(0x20)

class SSD1306_I2C(framebuf.FrameBuffer):
    def __init__(self, width, height, i2c, addr=0x3C):
        self.width = width
        self.height = height
        self.i2c = i2c
        self.addr = addr
        self.buffer = bytearray(self.height * self.width // 8)
        super().__init__(self.buffer, self.width, self.height, framebuf.MONO_VLSB)
        self.init_display()

    def write_cmd(self, cmd):
        self.i2c.writeto(self.addr, bytearray([0x80, cmd]))

    def init_display(self):
        for cmd in (
            DISPLAY_OFF,
            SET_DISPLAY_CLOCK_DIV, 0x80,
            SET_MULTIPLEX, self.height - 1,
            SET_DISPLAY_OFFSET, 0x00,
            SET_START_LINE | 0x00,
            SET_CHARGE_PUMP, 0x14,
            SET_MEMORY_MODE, 0x00,
            SET_SEGMENT_REMAP | 0x01,
            SET_COM_SCAN_DEC,
            SET_COM_PINS, 0x02 if self.height == 32 else 0x12,
            SET_CONTRAST, 0xCF,
            SET_PRECHARGE, 0xF1,
            SET_VCOM_DETECT, 0x40,
            SET_NORMAL_DISPLAY,
            DISPLAY_ON
        ):
            self.write_cmd(cmd)

    def show(self):
        for i in range(0, len(self.buffer), 16):
            self.i2c.writeto(self.addr, bytearray([0x40]) + self.buffer[i:i+16])
