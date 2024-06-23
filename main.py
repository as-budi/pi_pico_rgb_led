import neopixel
from machine import Pin
import time

ws_pin = 23
led_num = 1
BRIGHTNESS = 0.1  # Adjust the brightness (0.0 - 1.0)

neoRing = neopixel.NeoPixel(Pin(ws_pin), led_num)

def set_brightness(color):
    r, g, b = color
    r = int(r * BRIGHTNESS)
    g = int(g * BRIGHTNESS)
    b = int(b * BRIGHTNESS)
    return (r, g, b)

def loop():
    r = 0
    while (r < 256):
        g = 0
        while (g < 256):
            b = 0
            while (b < 256):          
                color = (r, g, b)  # Red color
                color = set_brightness(color)
                neoRing.fill(color)
                neoRing.write()
                time.sleep(0.1)
                b = b + 10
            g = g + 10
        r = r + 10

    # Display green
    #color = (0, 255, 0)  # Green color
    #color = set_brightness(color)
    #neoRing.fill(color)
    #neoRing.write()
    #time.sleep(1)

    # Display blue
    #color = (0, 0, 255)  # Blue color
    #color = set_brightness(color)
    #neoRing.fill(color)
    #neoRing.write()
    #time.sleep(1)

while True:
    loop()