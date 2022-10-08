from machine import Pin, I2C

from ssd1306 import SSD1306_I2C

from oled import Write, GFX, SSD1306_I2C

from oled.fonts import ubuntu_mono_15, ubuntu_mono_20

import utime




WIDTH =128

HEIGHT= 64 

i2c=I2C(0,scl=Pin(17),sda=Pin(16),freq=200000)

oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)

write15 = Write(oled, ubuntu_mono_15)

write20 = Write(oled, ubuntu_mono_20)

write20.text("Mr", 0, 0)

write15.text("Swastik Mishra", 0, 20)

oled.text("CSE-R 1941012339", 0, 40)

oled.show()



