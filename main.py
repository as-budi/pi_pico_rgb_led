import neopixel
from machine import Pin
import time

ws_pin = 16
led_num = 1
BRIGHTNESS = 0.1  # Adjust the brightness (0.0 - 1.0)

red = (255, 0, 0)
orange = (255, 50, 0)
yellow = (255, 100, 0)
green = (0, 255, 0)
blue = (0, 0, 255)
indigo = (100, 0, 90)
violet = (200, 0, 100)

colors = [red, orange, yellow, green, blue, indigo, violet]

neoRing = neopixel.NeoPixel(Pin(ws_pin), led_num)

def set_brightness(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (r, g, b)

def loop():
    for color in colors:
        color = set_brightness(color)
        neoRing.fill(color)
        neoRing.write()
        time.sleep(1)
    
#     # Display green
#     color = (255, 0, 0)  # Green color
#     color = set_brightness(color)
#     neoRing.fill(color)
#     neoRing.write()
#     time.sleep(1)
# 
#     # Display green
#     color = (0, 255, 0)  # Green color
#     color = set_brightness(color)
#     neoRing.fill(color)
#     neoRing.write()
#     time.sleep(1)
# 
#     # Display blue
#     color = (0, 0, 255)  # Blue color
#     color = set_brightness(color)
#     neoRing.fill(color)
#     neoRing.write()
#     time.sleep(1)

while True:
    loop()