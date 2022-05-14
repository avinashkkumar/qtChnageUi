import sys
from PyQt5.uic import loadUi
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QDialog, QApplication

class firstScreen(QDialog):
    def __init__(self):
        super(firstScreen,self).__init__()
        loadUi("first_window.ui",self)
        self.pushButton.clicked.connect(self.gsc2)

    def gsc2(self):
        widget.setCurrentIndex(1)



class secondScreen(QDialog):
    def __init__(self):
        super(secondScreen, self).__init__()
        loadUi("second_window.ui", self)
        self.pushButton.clicked.connect(self.gsc1)


    def gsc1(self):
        widget.setCurrentIndex(0)


app = QApplication(sys.argv)
widget = QtWidgets.QStackedWidget()
screen1=firstScreen()
screen2=secondScreen()
# adding all the widgets in application in order to make sure all the widget are there and then changing the widget index from the class
# do remember that the index starts with the index of 0
widget.addWidget(screen1)
widget.addWidget(screen2)

# setting the minimum hight and width to make sure that the window that is used in here is resizeable 
# the size in this case is can be increased but not decreased lower then the specified size
widget.setMinimumHeight(450)
widget.setMinimumWidth(600)
widget.show()
app.exec_()