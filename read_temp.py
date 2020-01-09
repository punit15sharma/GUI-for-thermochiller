from serial import Serial
import time
import binascii

chiller = Serial("/dev/ttyUSB0", timeout=1)

read_temp = bytearray([0xCA, 0x00, 0x01, 0x70, 0x00, 0x8E])
chiller.write(read_temp)
code_status = chiller.read(18)
print(binascii.hexlify(code_status))
