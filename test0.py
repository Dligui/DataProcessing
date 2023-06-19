from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QApplication, QMainWindow , QPushButton, QTableWidget, QTableWidgetItem , QHeaderView, QHBoxLayout, QVBoxLayout
#from PyQt5.QtCore import slot
import pandas as pd 
import sys
#****************my class************************** connect button to our label*****
class Mywindow(QMainWindow):
    def __init__(self): # constructeur 
        super(Mywindow, self).__init__() # super() makes it easier for other classes to use the class you're writing.
        self.setGeometry(300,400,300,300) # (xpos,ypos,width,height)
        self.setWindowTitle("MY FIRST GUI")
        self.initUI()
    
    def initUI(self):
        self.label1=QtWidgets.QLabel(self)
        self.label1.setText(" Hi it's me Ghizlan ! ")
        self.label1.move(100,100)

        self.button1=QtWidgets.QPushButton(self)
        self.button1.setText("click here")
        self.button1.clicked.connect(self.clicked) #signals 

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self): # to update the size of our label
        self.label.adjustSize()

#*********************Main programm***************************************
def demo ():
    app=QApplication(sys.argv)
    win=Mywindow()
    win.show()
    sys.exit(app.exec_())

demo()









