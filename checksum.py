'''
Diksha Garg
Nov 13 2019
Comment: This program calculates checksum
Notes: 
a) If there is one bit then it gets added with 0 automatically when it is represented as 0x form. 
b) We finally just calculated d1, d2 nd checksum and then just transported the value to read_status.py program and it used in its array to finally send out the command.'''

import numpy
import binascii
from temperature_bites import d1, d2

data = bytearray([0xCA,0x00,0x01,0xF0,0x02,int(d1,16),int(d2,16)])
print(data)
sum_int = (sum(data[1:])) #not including CA in the sum 

print("sum in dec = " + str(sum_int))  #this is in decimal form and int
print("sum in hex = " + str(hex(sum_int))) #in hex form and in int

hex_num = format(sum_int, 'x') #now it is in hex form and string
print("sum in hex = " + hex_num)

#doing XOR
b = 'ff' #this is the number with which we will do XOR

#taking only two LSB of the hex sum
if len(hex_num)>2:
    num_1 = hex_num[1]
    num_2 = hex_num[2]
    sum_hex = ('{}{}'.format(num_1,num_2))
    
    #c = abs(int(a,16))%100   #this is sum in hex but only last 2 LSB
    print("sum in hex w/ lsb= " + sum_hex)#str(c))
    checksum = '%x' % (int(sum_hex,16)^int(b,16))  #in this c,b should be of string type
    print("checksum = " + checksum)
    
else:
    print("sum in hex w/o lsb = " + hex_num)
    checksum = '%x' % (int(hex_num,16)^int(b,16))
    print("checksum = " + checksum)

print('%x' % int(checksum,16))

#appending checksum value to the array
setpoint_int = numpy.append(data,int(checksum,16))
print(setpoint_int)

#changing every element of setpoint_int array to a hexadecimal string
setpoint = [hex(x) if x>15 else "{:#04x}".format(x) for x in setpoint_int]
print(setpoint)



'''
j=0  #counter

setpoint_int = setpoint_int.astype(numpy.float)
#print(type(setpoint_int))

for i in setpoint_int:
    setpoint = numpy.append(setpoint, hex(setpoint_int[j])) #these elemets in setpoint array are interpreted as strings and not integers. FIX THAT! 
    j+=1



print(type(setpoint[0]))
print(setpoint)
#the elements in the array are being sent as a string rather than as int type. 
#print(s)

'''



'''
chiller = Serial("/dev/ttyUSB0", timeout=2)

chiller.write(setpoint)
'''





'''j=0
for i in range(len(setpoint)):
    setpoint[i] = arr[j]
    arr[j] = '%x' % int(setpoint[i],16)
    print(setpoint[i])
    j+=1
'''











'''
at = format(s,'x') #converted it into hex and removed 0x; in string form
ast = int(at)
#if len(s)>2:   

#d = hex(s)
n = bytearray('\xff',encoding='utf8')

checksum = hex(0xast^0xff)#in this way 0xat is not valid, but if I just pass at with 0xblah blah then it is in a string form. then xor between string and int doesn't happen.
'''
#print(checksum)
'''checksum = 0
for ch in data:
    checksum += (ch)

print(checksum)
'''
