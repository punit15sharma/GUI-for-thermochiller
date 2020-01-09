from serial import Serial

import sys
from PyQt5 import QtCore, QtWidgets
from PyQt5.QtWidgets import QMainWindow, QWidget, QLabel, QLineEdit
from PyQt5.QtWidgets import QPushButton
from PyQt5.QtCore import QSize    
#import temperature_bites

chiller = Serial("/dev/ttyUSB0", timeout=1)

class MainWindow(QMainWindow):
    
    def __init__(self):
        QMainWindow.__init__(self)

        self.setMinimumSize(QSize(400, 180))    
        self.setWindowTitle("ThermoChiller") 

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Temperature:')
        self.line = QLineEdit(self)

        self.line.move(110, 90)
        self.line.resize(50, 32)  #determines the size of the button/label's length (x,y)
        self.nameLabel.move(20, 90) #position on the panel (x,y)

        pybutton = QPushButton('Set', self)
        pybutton.clicked.connect(self.clickMethod)
        pybutton.resize(50,32)
        pybutton.move(110, 130)        

        self.nameLabel = QLabel(self)
        self.nameLabel.setText('Chiller:')
        self.nameLabel.move(20, 20)
                            
        on = QPushButton('On',self)
        on.clicked.connect(self.on_click)
        on.resize(50,32)
        on.move(110,20)

        off = QPushButton('Off',self)
        off.clicked.connect(self.off_click)
        off.resize(50,32)
        off.move(180,20) 

    def on_click(self):
        turn_on_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x01, 0x7B])
        turn_on = chiller.write(turn_on_data)
        turn_on_status = chiller.read(18)

    def off_click(self):
        turn_off_data = bytearray([0xCA, 0x00, 0x01, 0x81, 0x01, 0x00, 0x7C])
        turn_off = chiller.write(turn_off_data)
        turn_off_status = chiller.read(18)
        
    def clickMethod(self):
        global temp
        temp = self.line.text()
        #print(temp)
    #clickMethod(self)
    
    #print(temp)

if __name__ == "__main__":
    print("this")
    app = QtWidgets.QApplication(sys.argv)
    mainWin = MainWindow()
    print("this1")
    mainWin.show()
    print("this2")
    #sys.exit( app.exec_() )
    app.exec_()
    print("this3")
    temperature = MainWindow.clickMethod
    print(temperature)
#When we try to import temp in temperature_bites, we can't do that because as soon as GUI is implemented there is no temp value that exists but temp_bites is trying to read it. 
