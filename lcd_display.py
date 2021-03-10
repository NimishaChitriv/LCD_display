import utime
from lcd_api import LcdApi
from machine import I2C,Pin,ADC
from pico_i2c_lcd import I2cLcd

I2C_ADDR=0x27
I2C_NUM_ROWS= 4
I2C_NUM_COLS= 20

sense_temp=ADC(4)
conversion_factor=3.3/65535

i2c=I2C(0,sda=Pin(0),scl=Pin(1),freq=400000)

lcd = I2cLcd(i2c, I2C_ADDR, I2C_NUM_ROWS, I2C_NUM_COLS) 

while True:
    
    voltage=sense_temp.read_u16()*conversion_factor
    temp_C=27-(voltage-0.706)/0.001721
    print(temp_C)
   
    
    temp_F= (temp_C*9/5)+32
    print(temp_F)
    
    
    lcd.clear()
    lcd.move_to(0,0)
    lcd.putstr("Temp in C = {0:5.2f}".format(temp_C))
    lcd.move_to(0,1)
    lcd.putstr("Temp in F = {0:5.2f}" .format(temp_F))
    utime.sleep(2)
    
    
    


