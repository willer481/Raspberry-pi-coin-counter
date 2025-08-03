# SSD1306 OLED Driver for MicroPython 🎮🖥️

A lightweight MicroPython driver for SSD1306 OLED displays, tested on a 128x32 screen using I²C with a Raspberry Pi Pico. Designed for simplicity and fast setup!

## 📦 Features
- Works with 128x32 pixel SSD1306 OLEDs over I²C
- FrameBuffer-based rendering
- Easy plug-and-play with MicroPython
- Clean initialization and refresh logic

## 🛠️ Setup
Upload `ssd1306.py` to your Raspberry Pi Pico using [Thonny](https://thonny.org/), and you're ready to go!

```python
from machine import I2C, Pin
from ssd1306 import SSD1306_I2C

i2c = I2C(0, scl=Pin(17), sda=Pin(16))
oled = SSD1306_I2C(128, 32, i2c)
oled.text("Hello World!", 0, 0)
oled.show()

🔗 Follow Me!
I'm Willem — a 13-year-old coder from the UK who loves Python, MicroPython, and 3D modeling. This is just one of many projects I'm working on!

🧠 GitHub: willer481

🎬 YouTube: @Rox_Playz_Blox

☕ Ko-fi: Support my work

If this helped you or you’d like to support me, feel free to subscribe, follow, or donate!

🤝 License
This code is AI-assisted (thanks Copilot!), but open to all. Feel free to modify, share, and credit however you want.

Thanks for checking out my project! 🚀
