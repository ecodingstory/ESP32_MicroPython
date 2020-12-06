from machine import Pin
led_0= Pin(16, Pin.OUT)
led_1 = Pin(17, Pin.OUT)
button_0 = Pin(4, Pin.IN)
button_1 = Pin(5, Pin.IN)

while True:
  if(button_0.value()):
    led_0.on()
  else:
    led_0.off()
  if(button_1.value()):
    led_1.on()
  else:
    led_1.off()  
