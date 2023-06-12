import psutil

def get_system_stats():
    cpu_usage = psutil.cpu_percent()
    mem_usage = psutil.virtual_memory().percent
    #disk_usage = psutil.disk_usage('/').percent
    return cpu_usage, mem_usage

def display_system_stats(LCD_DEVICE, cpu_usage, mem_usage):
    LCD_DEVICE.cursor_pos = (0, 0)
    LCD_DEVICE.write_string(f'CPU: {cpu_usage}%')
    LCD_DEVICE.cursor_pos = (1, 0)
    LCD_DEVICE.write_string(f'MEM: {mem_usage}%')
