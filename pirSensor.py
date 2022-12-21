from machine import Pin
import time
 
pir = Pin(16, Pin.IN, Pin.PULL_DOWN)
led = Pin(25, Pin.OUT)
n = 0
 
print('Starting up the PIR Module')
time.sleep(1)
led.low()
print('Ready')
 
while True:
     led.low()
     if pir.value() == 1:
          n = n+1
          print('Motion Detected ',n)
          led.high()
          
     time.sleep(1)
     
