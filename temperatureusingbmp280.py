
from machine import Pin,I2C
from bmp280 import *
from ssd1306 import SSD1306_I2C
import time

bus = I2C(0,sda=Pin(0), scl=Pin(1), freq=400000)
bmp = BMP280(bus)

bmp.use_case(BMP280_CASE_INDOOR)

WIDTH =128                     
HEIGHT= 64
i2c=I2C(0,scl=Pin(1),sda=Pin(0),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

while True:
    pressure=bmp.pressure
    p_bar=pressure/100000
    p_mmHg=pressure/133.322
    temperature=bmp.temperature
    oled.text("Temperature:", 0, 0)
    oled.text(str(temperature)+" C", 50, 15)
    oled.text("Pressure:", 0, 30)
    oled.text(str(pressure)+" Pa", 40, 45)
    oled.show()
    time.sleep(1)
    oled.fill(0)


