from time import sleep
# fetch temperature and humidity from dht11 sensor
def get_dht11_data(DHT_DEVICE):
    while True :
        try:
            temperature = DHT_DEVICE.temperature
            humidity = DHT_DEVICE.humidity
            return temperature, humidity
        except RuntimeError as error:
            print(error.args[0])
            sleep(2.0)
            continue
        except Exception as error:
            DHT_DEVICE.exit()
            raise error


# display temperature and humidity from dht11 sensor to lcd1602 display
def display_dht11_data(LCD_DEVICE, temperature, humidity):
    LCD_DEVICE.cursor_pos = (0, 0)
    LCD_DEVICE.write_string(f'Temp: {temperature}\x07C')
    LCD_DEVICE.cursor_pos = (1, 0)
    LCD_DEVICE.write_string(f'Hum:  {humidity}%')
