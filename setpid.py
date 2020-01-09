# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'SetPID.ui'
#
# Created by: PyQt5 UI code generator 5.13.0
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_Form(object):
    def setupUi(self, Form):
        Form.setObjectName("Form")
        Form.resize(259, 179)
        self.Psetting = QtWidgets.QDoubleSpinBox(Form)
        self.Psetting.setGeometry(QtCore.QRect(130, 20, 62, 22))
        self.Psetting.setMinimum(0.1)
        self.Psetting.setMaximum(99.9)
        self.Psetting.setProperty("value", 0.1)
        self.Psetting.setObjectName("Psetting")
        self.Isetting = QtWidgets.QDoubleSpinBox(Form)
        self.Isetting.setGeometry(QtCore.QRect(130, 60, 62, 22))
        self.Isetting.setMaximum(9.99)
        self.Isetting.setObjectName("Isetting")
        self.Dsetting = QtWidgets.QDoubleSpinBox(Form)
        self.Dsetting.setGeometry(QtCore.QRect(130, 100, 62, 22))
        self.Dsetting.setMaximum(5.0)
        self.Dsetting.setSingleStep(0.1)
        self.Dsetting.setObjectName("Dsetting")
        self.label = QtWidgets.QLabel(Form)
        self.label.setGeometry(QtCore.QRect(20, 20, 91, 21))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Form)
        self.label_2.setGeometry(QtCore.QRect(60, 60, 41, 21))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(Form)
        self.label_3.setGeometry(QtCore.QRect(50, 100, 51, 21))
        self.label_3.setObjectName("label_3")
        self.SetPID = QtWidgets.QPushButton(Form)
        self.SetPID.setGeometry(QtCore.QRect(130, 140, 61, 31))
        self.SetPID.setObjectName("SetPID")

        self.retranslateUi(Form)
        QtCore.QMetaObject.connectSlotsByName(Form)

    def retranslateUi(self, Form):
        _translate = QtCore.QCoreApplication.translate
        Form.setWindowTitle(_translate("Form", "Form"))
        self.label.setText(_translate("Form", "Proportional Band"))
        self.label_2.setText(_translate("Form", "Integral"))
        self.label_3.setText(_translate("Form", "Derivative"))
        self.SetPID.setText(_translate("Form", "Set PID"))


if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    Form = QtWidgets.QWidget()
    ui = Ui_Form()
    ui.setupUi(Form)
    Form.show()
    sys.exit(app.exec_())
