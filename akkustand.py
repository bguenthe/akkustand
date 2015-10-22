# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'akkustand.ui'
#
# Created: Mon Jun 23 18:21:10 2014
#      by: PyQt5 UI code generator 5.3
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_Dialog(object):
    def setupUi(self, Dialog):
        Dialog.setObjectName("Dialog")
        Dialog.resize(917, 572)
        self.buttonBox = QtWidgets.QDialogButtonBox(Dialog)
        self.buttonBox.setGeometry(QtCore.QRect(290, 510, 261, 32))
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Cancel|QtWidgets.QDialogButtonBox.Ok)
        self.buttonBox.setObjectName("buttonBox")
        self.label = QtWidgets.QLabel(Dialog)
        self.label.setGeometry(QtCore.QRect(20, 20, 151, 22))
        self.label.setObjectName("label")
        self.label_2 = QtWidgets.QLabel(Dialog)
        self.label_2.setGeometry(QtCore.QRect(20, 50, 151, 22))
        self.label_2.setObjectName("label_2")
        self.percent = QtWidgets.QLabel(Dialog)
        self.percent.setGeometry(QtCore.QRect(120, 20, 74, 22))
        self.percent.setLineWidth(1)
        self.percent.setObjectName("percent")
        self.time = QtWidgets.QLabel(Dialog)
        self.time.setGeometry(QtCore.QRect(120, 50, 74, 22))
        self.time.setLineWidth(1)
        self.time.setObjectName("time")
        self.label_3 = QtWidgets.QLabel(Dialog)
        self.label_3.setGeometry(QtCore.QRect(210, 20, 31, 22))
        self.label_3.setObjectName("label_3")
        self.label_4 = QtWidgets.QLabel(Dialog)
        self.label_4.setGeometry(QtCore.QRect(210, 50, 71, 22))
        self.label_4.setObjectName("label_4")
        self.timetable = QtWidgets.QTableWidget(Dialog)
        self.timetable.setGeometry(QtCore.QRect(20, 100, 871, 381))
        self.timetable.setAutoFillBackground(False)
        self.timetable.setObjectName("timetable")

        self.retranslateUi(Dialog)
        self.buttonBox.accepted.connect(Dialog.accept)
        self.buttonBox.rejected.connect(Dialog.reject)
        QtCore.QMetaObject.connectSlotsByName(Dialog)

    def retranslateUi(self, Dialog):
        _translate = QtCore.QCoreApplication.translate
        Dialog.setWindowTitle(_translate("Dialog", "Dialog"))
        self.label.setText(_translate("Dialog", "Restlaufzeit"))
        self.label_2.setText(_translate("Dialog", "Restlaufzeit"))
        self.percent.setText(_translate("Dialog", "TextLabel"))
        self.time.setText(_translate("Dialog", "TextLabel"))
        self.label_3.setText(_translate("Dialog", "%"))
        self.label_4.setText(_translate("Dialog", "Stunden"))

