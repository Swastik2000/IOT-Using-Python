from machine import Pin, UART, I2C
from ssd1306 import SSD1306_I2C
from oled import Write

from oled.fonts import ubuntu_mono_15, ubuntu_mono_20

uart = UART(0, 9600)
led = Pin(16, Pin.OUT)


WIDTH =128                     
HEIGHT= 64
i2c=I2C(0,scl=Pin(17),sda=Pin(12),freq=200000)
oled = SSD1306_I2C(WIDTH,HEIGHT,i2c)
write20 = Write(oled, ubuntu_mono_20)


while True:
  if uart.any() > 0:
    data = uart.read()
    
    if "on" in data:
      led.value(1)
      print('LED on \n')
      uart.write('LED on \n')
      oled.fill(0)
      oled.show()
    elif "off" in data:
      led.value(0)
      print('LED off \n')
      uart.write('LED off \n')
      oled.fill(0)
      oled.show()
    else:
        text=data.strip()
        print(text)
        text=str(text)
        write20.text(text, 0, 0)
        oled.text(text, 0, 20)
        oled.show()

