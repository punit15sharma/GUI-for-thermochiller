from serial import Serial
from PyQt5.QtWidgets import *
#from checksum import d1, d2, checksum

chiller = Serial("/dev/ttyUSB0", timeout=1)

app = QApplication([])

window = QWidget()
layout = QVBoxLayout()

on = QPushButton('On')
off = QPushButton('Off')
#setpoint = QPushButton('Temperature')

layout.addWidget(on)
layout.addWidget(off)
#layout.addWidget(setpoint)
    
def on_click():
    turn_on_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x01, 0x7B])
    turn_on = chiller.write(turn_on_data)
    turn_on_status = chiller.read(18)

def off_click():
    turn_off_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x00, 0x7C])
    turn_off = chiller.write(turn_off_data)
    turn_off_status = chiller.read(18)

'''
def set_point_click():
    set_point_data = bytearray([0xCA, 0x00, 0x01, 0xF0, 0x02, int(d1,16), int(d2,16), int(checksum,16)])
    set_point = chiller.write(set_point_data)
    set_point_status = chiller.read(18)
'''

on.clicked.connect(on_click)
#on.show()

off.clicked.connect(off_click)
#off.show()

#setpoint.clicked.connect(set_point_click)

window.setLayout(layout)
window.show()
app.exec_()


