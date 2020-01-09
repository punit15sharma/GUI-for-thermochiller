#from serial import Serial
import time
import binascii
from checksum import d1, d2, checksum

#chiller = Serial("/dev/ttyUSB0", timeout=1)

'''
turn_on = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x01, 0x7B])
chiller.write(turn_on)
code_turn_on = chiller.read(18)
#print(binascii.hexlify(code_turn_on))
'''
"""
read_status = bytearray([0xCA, 0x00, 0x01,0x09, 0x00, 0xF5])
chiller.write(read_status)
code_status = chiller.read(18)
print(binascii.hexlify(code_status))"""

#setting temperature on chiller using checksum.py code 
set_point = bytearray([0xCA, 0x00, 0x01, 0xF0, 0x02, int(d1,16), int(d2,16), int(checksum,16)])
print(set_point)
#chiller.write(set_point)
#setpoint_status = chiller.read(18)
#print(binascii.hexlify(setpoint_status))



