import utime
from machine import Pin,I2C,
from lcd_api import LcdApi
from pico_i2c_lcd import I2cLcd

I2C_ADDR     = 0x27
I2C_NUM_ROWS = 4
I2C_NUM_COLS = 20




i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)

lcd=I2cLcd(i2c,I2C_ADDR,I2C_NUM_ROWS,I2C_NUM_COLS)


   
    
while True:
    lcd.clear()
    lcd.move_to(2,0)
    lcd.putstr("Hello World")
    utime.sleep(2)

    




    