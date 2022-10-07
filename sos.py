from machine import Pin
import utime
led = Pin(15, Pin.OUT)
#. 0.25 seconds
# gap 0.2
# line 1 sec

def s():
    i=3
    while i>0:
        led.toggle()
        utime.sleep(1)
        led.value(0)
        utime.sleep(0.2)
        i-=1
def o():
    i=3
    while i>0:
        led.toggle()
        utime.sleep(0.25)
        led.value(0)
        utime.sleep(0.2)
        i-=1

# while True:
#     s()
#     o()
#     s()
s()
led.value(0)
o()
led.value(0)
s()
led.value(0)
