'''
Diksha Garg
Nov 12 2019
Comments: 
1) This code takes input of the temperature and converts it into hexadecimal form. 
2) Then pads the temperature into two terms of two bits each, d1 and d2 (eg: 00 and 00) 
'''

import time
import textbox
#from textbox import MainWindow
print("did this print")
temperature = MainWindow.clickMethod
print
#convert decimal into hex and omits 0x in the beginning
temperature_hex = format(temperature, 'x')                        
print("temperature in hex = " + temperature_hex)

d2 = hex(temperature)
d1 = hex(0)
'''
#padding d1 ad d2 bits 
if len(temperature_hex)==1:
    d2_hex = str(temperature_hex).zfill(2)
    d1_hex = str(0).zfill(2)

if len(temperature_hex)==2:
    d2_hex = temperature_hex
    d1_hex = str(0).zfill(2)
    
d1_int = int(d1_hex)
d2_int = int(d2_hex)

d2 = hex(d1_int)
d1 = hex(d2_int)'''
print(d2, d1)
#print(d1, d2)  
   
