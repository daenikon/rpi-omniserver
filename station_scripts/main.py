import os
from adafruit_dht import DHT11
from RPLCD.i2c import CharLCD
from gpiozero import Button
from signal import pause
from time import sleep
import board

# custom modules
import sys
sys.path.append('/home/admin/python_scripts/station/modules/')
from chars import draw, face, file
from dht11 import get_dht11_data, display_dht11_data
from system_stats import get_system_stats, display_system_stats


def display_page1():
    global page_number
    if page_number != 1:
        return
    LCD_DEVICE.clear()
    draw(LCD_DEVICE, face)
    temperature, humidity = get_dht11_data(DHT11_DEVICE)
    display_dht11_data(LCD_DEVICE, temperature, humidity)

def display_page2():
    global page_number
    if page_number != 2:
        return
    LCD_DEVICE.clear()
    draw(LCD_DEVICE, file)
    cpu_usage, mem_usage = get_system_stats()
    display_system_stats(LCD_DEVICE, cpu_usage, mem_usage)

def switch_page():
    global page_number
    if page_number == 1:
        page_number = 2
        display_page2()
    else:
        page_number = 1
        display_page1()


LCD_DEVICE = CharLCD('PCF8574', 0x27)
DHT11_DEVICE  = DHT11(board.D17, use_pulseio=False)
BUTTON = Button(13)

page_number = 1

BUTTON.when_pressed = switch_page

while True:
    if page_number == 1:
        display_page1()
        sleep(300.0) # sleep for 5 minutes
    else:
        display_page2()
        sleep(30.0) # sleep for 30 seconds

pause()
