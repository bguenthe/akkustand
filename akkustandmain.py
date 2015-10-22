import os
import win32con
import sys
import time
from ctypes import *
import sys
from PyQt5 import QtCore, QtGui, QtWidgets
from akkustand import *


class PowerClass(Structure):
    _fields_ = [('ACLineStatus', c_byte),
                ('BatteryFlag', c_byte),
                ('BatteryLifePercent', c_byte),
                ('Reserved1', c_byte),
                ('BatteryLifeTime', c_ulong),
                ('BatteryFullLifeTime', c_ulong)]


class MeinDialog(QtWidgets.QDialog, Ui_Dialog):
    def __init__(self):
        QtWidgets.QDialog.__init__(self)
        self.ctimer = QtCore.QTimer()
        self.setupUi(self)
        self.ctimer.timeout.connect(self.constantUpdate)
        self.ctimer.start(1000 * 60)  # Pro minute
        self.powerclass = PowerClass()
        self.akkustandfile = open("./Akkustand.txt", "w")

        self.timetable.setColumnCount(3)
        self.rowcount = 0

        self.constantUpdate()

    def constantUpdate(self):
        result = windll.kernel32.GetSystemPowerStatus(byref(self.powerclass))

        try:
            percent = int(self.powerclass.BatteryLifePercent)
            blt = int(self.powerclass.BatteryLifeTime)
            blts = time.strftime('%H:%M:%S', time.gmtime(blt))
            stime = time.strftime("%d.%m.%Y um %H:%M:%S")
            self.akkustandfile.write("Uhrzeit: " + stime + "\t\tRestlaufzeit(%): " + str(
                percent) + "\t\tRestlaufzeit(Stunden): " + blts + "\n")
            self.akkustandfile.flush()

            self.rowcount = self.rowcount + 1
            self.timetable.setRowCount(self.rowcount)
            self.timetable.setItem(self.rowcount - 1, 0, QtWidgets.QTableWidgetItem(stime))
            self.timetable.setItem(self.rowcount - 1, 1, QtWidgets.QTableWidgetItem(str(percent)))
            self.timetable.setItem(self.rowcount - 1, 2, QtWidgets.QTableWidgetItem(blts))
        except Exception as e:
            print(e)
            percent = 0

        self.percent.setText(str(percent))
        self.time.setText(blts)


app = QtWidgets.QApplication(sys.argv)
dialog = MeinDialog()
dialog.show()
sys.exit(app.exec_())