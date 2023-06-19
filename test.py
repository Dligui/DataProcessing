
from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QMessageBox # to create a pop up 
import pandas as pd 

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 600)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.button = QtWidgets.QPushButton(self.centralwidget)
        self.button.setGeometry(QtCore.QRect(300, 260, 141, 71))
        self.button.setObjectName("button")
        self.label = QtWidgets.QLabel(self.centralwidget)
        self.label.setGeometry(QtCore.QRect(320, 80, 191, 111))
        self.label.setObjectName("label")
        MainWindow.setCentralWidget(self.centralwidget)
        self.menubar = QtWidgets.QMenuBar(MainWindow)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 800, 21))
        self.menubar.setObjectName("menubar")
        self.menuFile = QtWidgets.QMenu(self.menubar)
        self.menuFile.setObjectName("menuFile")
        MainWindow.setMenuBar(self.menubar)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)
        self.actionSave = QtWidgets.QAction(MainWindow)
        self.actionSave.setObjectName("actionSave")
        self.actionRecall = QtWidgets.QAction(MainWindow)
        self.actionRecall.setObjectName("actionRecall")
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionRecall)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

        self.button.clicked.connect(self.show_popup)
   

    def show_popup(self):
        msg=QMessageBox()
        msg.setWindowTitle("This is a popup") 
        msg.setText("this is the main text of ur popup ! ")
        x=msg.exec_()

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.button.setText(_translate("MainWindow", "Press Me !"))
        self.label.setText(_translate("MainWindow", "Hi it\'s me ghizlane"))
        self.menuFile.setTitle(_translate("MainWindow", "File"))
        self.actionSave.setText(_translate("MainWindow", "Save"))
        self.actionRecall.setText(_translate("MainWindow", "Recall"))
        self.button.setText(_translate("MainWindow", " Show Popup"))

if __name__ == "__main__":
    import sys
    app = QtWidgets.QApplication(sys.argv)
    MainWindow = QtWidgets.QMainWindow()
    ui = Ui_MainWindow()
    ui.setupUi(MainWindow)
    MainWindow.show()
    try:
        sys.exit(app.exec_())
    execpt SystemExit:
    print('Closing Window...')
