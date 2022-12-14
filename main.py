# Form implementation generated from reading ui file 'untitled.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.
import sys
import time

from PyQt6 import QtCore, QtGui, QtWidgets
from tkinter import *
import winsound
import threading

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.pushButton = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton.setGeometry(QtCore.QRect(480, 50, 75, 23))
        self.pushButton.setObjectName("pushButton")
        self.progressBar = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar.setGeometry(QtCore.QRect(570, 50, 118, 23))
        self.progressBar.setProperty("value", 0)
        self.progressBar.setObjectName("progressBar")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(30, 10, 411, 351))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap(":/sonidos/spike-valorant.gif"))
        self.label.setScaledContents(True)
        self.label.setObjectName("label")
        self.progressBar_2 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_2.setGeometry(QtCore.QRect(30, 380, 441, 23))
        self.progressBar_2.setProperty("value", 0)
        self.progressBar_2.setFormat("")
        self.progressBar_2.setObjectName("progressBar_2")
        self.lcdNumber = QtWidgets.QLCDNumber(self.centralwidget)
        self.lcdNumber.setGeometry(QtCore.QRect(440, 380, 64, 23))
        self.lcdNumber.setFrameShape(QtWidgets.QFrame.Shape.StyledPanel)
        self.lcdNumber.setDigitCount(5)
        self.lcdNumber.setSegmentStyle(QtWidgets.QLCDNumber.SegmentStyle.Filled)
        self.lcdNumber.setProperty("value", 0.0)
        self.lcdNumber.setObjectName("lcdNumber")
        self.progressBar_3 = QtWidgets.QProgressBar(self.centralwidget)
        self.progressBar_3.setGeometry(QtCore.QRect(350, 410, 118, 23))
        self.progressBar_3.setProperty("value", 0)
        self.progressBar_3.setObjectName("progressBar_3")
        self.pushButton_2 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_2.setGeometry(QtCore.QRect(270, 410, 75, 23))
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalSlider = QtWidgets.QSlider(self.centralwidget)
        self.verticalSlider.setGeometry(QtCore.QRect(470, 90, 22, 121))
        self.verticalSlider.setOrientation(QtCore.Qt.Orientation.Vertical)
        self.verticalSlider.setObjectName("verticalSlider")
        self.label_2 = QtWidgets.QLabel(self.centralwidget)
        self.label_2.setGeometry(QtCore.QRect(510, 140, 47, 13))
        self.label_2.setObjectName("label_2")
        self.pushButton_3 = QtWidgets.QPushButton(self.centralwidget)
        self.pushButton_3.setGeometry(QtCore.QRect(670, 500, 75, 23))
        self.pushButton_3.setObjectName("pushButton_3")
        self.label_3 = QtWidgets.QLabel(self.centralwidget)
        self.label_3.setGeometry(QtCore.QRect(640, 390, 141, 101))
        self.label_3.setObjectName("label_3")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "Spike"))
        self.pushButton.setText(_translate("MainWindow", "Plantar"))
        self.pushButton_2.setText(_translate("MainWindow", "Desplantar"))
        self.label_2.setText(_translate("MainWindow", "Volumen"))
        self.pushButton_3.setText(_translate("MainWindow", "A"))
        self.label_3.setText(_translate("MainWindow", ""))


class myapp(QtWidgets.QMainWindow,Ui_MainWindow):

    plantstatus=0
    explo=0

    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        Ui_MainWindow.__init__(self)
        self.setupUi(self)
        self.pushButton.clicked.connect(self.plantar)
        self.pushButton_2.clicked.connect(self.defuse)

    def plantar(self):
        self.plantstatus=1
        winsound.PlaySound('plant.wav', winsound.SND_ASYNC)
        self.label_3.setText("Plantando Spike")
        for i in range(101):
            time.sleep(0.02)
            self.progressBar.setValue(i)
        self.label_3.setText("Spike plantada")
        self.pushButton.setEnabled(False)
        Movie = QtGui.QMovie("spike-valorant.gif")
        Movie.start()
        self.label.setMovie(Movie)

        hilo = threading.Thread(target=self.spiketimer, args=(), daemon=True)
        hilo.start()

    def spiketimer(self):
        self.plantstatus
        winsound.PlaySound('timer.wav',winsound.SND_ASYNC)
        timer=29.00
        percentaje=100
        while(percentaje>0):
            percentaje = (timer / 29) * 100
            time.sleep(0.01)
            timer-=0.01
            self.progressBar_2.setProperty("value", percentaje)
            self.lcdNumber.setProperty("value", timer)
            if(self.plantstatus==0):
                return
        Movie2 = QtGui.QMovie("spike-boom.gif")
        self.label.setPixmap(QtGui.QPixmap("spike-boom.gif"))
        Movie2.start()
        self.label.setMovie(Movie2)
        time.sleep(4)
        self.close()

    def defuse(self):
        winsound.PlaySound('defuse.wav', winsound.SND_ASYNC)
        for i in range(101):
            time.sleep(0.025)
            self.progressBar_3.setValue(i)
        self.plantstatus=0
        self.label_3.setText("Spike desactivada")
        self.pushButton.setEnabled(True)

if __name__ == "__main__":
    app=QtWidgets.QApplication(sys.argv)
    window=myapp()
    window.show()
    sys.exit(app.exec())

