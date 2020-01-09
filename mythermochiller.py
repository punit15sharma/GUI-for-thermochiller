# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mythermochilller.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


import serial
from serial import Serial
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from setpid import Ui_Form
from PyQt5.QtCore import QTimer

chiller = Serial("/dev/ttyUSB0", timeout=1)
def checksumm(d1, d2):
    data = bytearray([0xCA,0x00,0x01,0xF0,0x02, d1, d2])
    sum_int = (sum(data[1:]))
    hex_num = format(sum_int, 'x')
    b = 'ff'
    if len(hex_num)>2:
        num_1 = hex_num[1]
        num_2 = hex_num[2]
        sum_hex = ('{}{}'.format(num_1,num_2))
        checksum = '%x' % (int(sum_hex,16)^int(b,16))
    else:
        checksum = '%x' % (int(hex_num,16)^int(b,16))
    return checksum

def set_temp(d2):
    cs=checksumm(0,d2)
    if (d2>31):
        d1=0
        set_temp= bytearray([0xCA, 0x00, 0x01, 0xF0, 0x02, d1, d2, int(cs,16)])
        a=str(hex(d2))
        a=a[-2:]
        c=str(set_temp)
        d="')"
        m=str(cs)
        m=m[-2:]
        return(c[:-7]+'\\x'+a+'\\x'+m+d)
    else:
        output = bytearray([0xCA, 0x00, 0x01, 0xF0, 0x02, 0x00, d2, int(cs,16)])
        return output




class Ui_ThermoChiller(object):
    def onclickedpid(self):
        self.window = QtWidgets.QMainWindow()
        self.ui = Ui_Form()
        self.ui.setupUi(self.window)
        self.window.show()
    def on_click(self):
        turn_on_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x01, 0x7B])
        turn_on = chiller.write(turn_on_data)
        #turn_on_status = chiller.read(18)

    def off_click(self):
        turn_off_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x00, 0x7C])
        turn_off = chiller.write(turn_off_data)
        #turn_off_status = chiller.read(18)    
    def settemperature(self, tempval):
        d2 = tempval
        set_tempval=set_temp(d2)
        print(set_tempval)
        chiller.write(set_tempval)

    
    def updateTempLCD(self, val):
        self.Temperaturenow.display(val)
        
        

    
    
    
    def setupUi(self, ThermoChiller):
        ThermoChiller.setObjectName("ThermoChiller")
        ThermoChiller.resize(496, 241)
        
        self.centralwidget = QtWidgets.QWidget(ThermoChiller)
        self.centralwidget.setObjectName("centralwidget")
        
        self.onbutton = QtWidgets.QPushButton(self.centralwidget)
        self.onbutton.setGeometry(QtCore.QRect(240, 20, 91, 41))
        self.onbutton.setObjectName("onbutton")
        
        self.offbutton = QtWidgets.QPushButton(self.centralwidget)
        self.offbutton.setGeometry(QtCore.QRect(344, 20, 90, 41))
        self.offbutton.setObjectName("offbutton")
        
        self.Temperaturenow = QtWidgets.QLCDNumber(self.centralwidget)
        self.Temperaturenow.setGeometry(QtCore.QRect(30, 20, 151, 101))
        self.Temperaturenow.setObjectName("Temperaturenow")
        
        self.settempbutton = QtWidgets.QPushButton(self.centralwidget)
        self.settempbutton.setGeometry(QtCore.QRect(240, 160, 121, 41))
        self.settempbutton.setObjectName("settempbutton")
        #self.settempbutton.clicked.connect(lambda: self.updateTempLCD(settempval))
        #self.setvaluebutton.clicked.connect(lambda: self.updateQCD(self.rolling.value()))
        #self.settempbutton.clicked.connect(lambda: self.settemperature(settempval))
        
        
        self.TempSetting = QtWidgets.QSpinBox(self.centralwidget)
        self.TempSetting.setGeometry(QtCore.QRect(60, 160, 121, 41))
        self.TempSetting.setMinimum(5)
        self.TempSetting.setMaximum(100)
        self.TempSetting.setSingleStep(1)
        self.TempSetting.setObjectName("TempSetting")
        
        
        
        self.setpidbutton = QtWidgets.QPushButton(self.centralwidget)
        self.setpidbutton.setGeometry(QtCore.QRect(240, 80, 91, 41))
        self.setpidbutton.setObjectName("setpidbutton")
        
        ThermoChiller.setCentralWidget(self.centralwidget)
        self.actionSetPDI = QtWidgets.QAction(ThermoChiller)
        self.actionSetPDI.setObjectName("actionSetPDI")

        self.retranslateUi(ThermoChiller)
        QtCore.QMetaObject.connectSlotsByName(ThermoChiller)
        
        self.setpidbutton.clicked.connect(self.onclickedpid)
        self.onbutton.clicked.connect(self.on_click)
        self.offbutton.clicked.connect(self.off_click)
       # self.settempbutton.clicked.connect(self.settemp_click(settempval))
       
        self.settempbutton.clicked.connect(lambda: self.updateTempLCD(self.TempSetting.value()))
        #self.setvaluebutton.clicked.connect(lambda: self.updateQCD(self.rolling.value()))
        self.settempbutton.clicked.connect(lambda: self.settemperature(self.TempSetting.value()))
        

    def retranslateUi(self, ThermoChiller):
        _translate = QtCore.QCoreApplication.translate
        ThermoChiller.setWindowTitle(_translate("ThermoChiller", "MainWindow"))
        self.onbutton.setText(_translate("ThermoChiller", "ON"))
        self.offbutton.setText(_translate("ThermoChiller", "OFF"))
        self.settempbutton.setText(_translate("ThermoChiller", "Set Temperature"))
        self.setpidbutton.setText(_translate("ThermoChiller", "SET PID"))
        self.actionSetPDI.setText(_translate("ThermoChiller", "SetPDI"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    ThermoChiller = QtWidgets.QMainWindow()
    ui = Ui_ThermoChiller()
    ui.setupUi(ThermoChiller)
    ThermoChiller.show()
    sys.exit(app.exec_())
