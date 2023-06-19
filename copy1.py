from PyQt6 import QtCore, QtGui, QtWidgets
from PyQt6.QtWidgets import QDialog,QApplication,QFileDialog
import sys
from Copy11 import ui_MainWindow

class Main(QtGui.QMainWindow, ui_MainWindow):
    def __init__(self):
        QtGui.QMainWindow.__init__(self)
        self.setupUi(self)
        super(Main,self).__init__()
        #self.CopyData.clicked.connect(Paste_table_vf(fname[0]))
        self.Browse.clicked.connect(self.Browsefiles)

        def Browsefiles(self):
            fname=QFileDialog.getOpenFileName(self,'open file','.')
            self.Filename.setText(fname[0])

if __name__== "__main__":
    import sys
    app=QtWidgets.QApplication(sys.argv)
    form=QtWidgets.QWidget()
    ui=Main()
    ui.setupUi(form)
    form.show()
    sys.exit(app.exec())