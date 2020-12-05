from machine import Pin
from time import sleep
p2_led = Pin(2, Pin.OUT)
while True:
  p2_led.on()
  sleep(0.5)
  p2_led.off()
  sleep(0.5)
