from machine import Pin, I2C
import time
import ssd1306

# Coin values in pence
coins = {
    "1p": {"value": 1, "pin": 2},
    "2p": {"value": 2, "pin": 3},
    "5p": {"value": 5, "pin": 4},
    "10p": {"value": 10, "pin": 5},
    "20p": {"value": 20, "pin": 6},
    "50p": {"value": 50, "pin": 7},
    "£1": {"value": 100, "pin": 8},
    "£2": {"value": 200, "pin": 9}
}

# Set up I2C and OLED display
i2c = I2C(0, scl=Pin(17), sda=Pin(16))  # Adjust pins if needed
oled = ssd1306.SSD1306_I2C(128, 32, i2c)

# Coin counters
coin_counts = {key: 0 for key in coins}
total_pence = 0

# Button interrupt function
def coin_pressed(coin_key):
    global total_pence
    coin_counts[coin_key] += 1
    total_pence += coins[coin_key]["value"]
    update_display()

# Attach buttons
for coin_key, coin in coins.items():
    pin = Pin(coin["pin"], Pin.IN, Pin.PULL_UP)
    pin.irq(trigger=Pin.IRQ_FALLING, handler=lambda p, k=coin_key: coin_pressed(k))

# OLED update
def update_display():
    oled.fill(0)
    y = 0
    for coin, count in coin_counts.items():
        if y <= 16:
            oled.text(f"{coin}:{count}", 0, y)
            y += 8
    oled.text(f"Total: £{total_pence/100:.2f}", 0, 24)
    oled.show()

# Main loop
while True:
    time.sleep(0.1)
