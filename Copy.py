# Form implementation generated from reading ui file 'CopyData.ui'
#
# Created by: PyQt6 UI code generator 6.4.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QApplication,QFileDialog
import sys
class Ui_MainWindow(object):
    # def __init__(self):
    #     super(Ui_MainWindow,self).__init__()
    #     #self.CopyData.clicked.connect(Paste_table_vf(fname[0]))
    # def Browsefiles(self):
    #     fname=QFileDialog.getOpenFileName(self,'open file','.')
    #     self.Filename.setText(fname[0])

    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(815, 324)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(20, 20, 131, 61))
        self.label.setObjectName("label")
        self.CopyData = QtWidgets.QPushButton(self.centralwidget)
        self.CopyData.setGeometry(QtCore.QRect(200, 100, 281, 41))
        self.CopyData.setAutoFillBackground(True)
        self.CopyData.setObjectName("CopyData")
        self.Filename = QtWidgets.QLineEdit(self.centralwidget)
        self.Filename.setGeometry(QtCore.QRect(70, 30, 551, 51))
        self.Filename.setObjectName("Filename")
        self.Browse = QtWidgets.QPushButton(self.centralwidget)
        self.Browse.setGeometry(QtCore.QRect(640, 30, 151, 51))
        self.Browse.setAutoFillBackground(True)
        self.Browse.setObjectName("Browse")
        #self.Browse.clicked.connect(self.Browsefiles)

        #MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 815, 26))
        self.menubar.setObjectName("menubar")
        #MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        #MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.label.setText(_translate("MainWindow", "Path : "))
        self.CopyData.setText(_translate("MainWindow", "CopyData"))
        self.Browse.setText(_translate("MainWindow", "Browse"))


