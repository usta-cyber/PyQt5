import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow,QPushButton
from PyQt5.QtGui import QIcon

# Three Types of Windows are there Qwidget,QDialog,QMainWindow 
class WindowExample(QWidget):
    def __init__(self):
        super().__init__()
        # X, Y , W,H
        self.setGeometry(200,200,400,300)
        self.setWindowTitle("PYTHON WINDOW")
        self.setWindowIcon(QIcon('python.png'))
    # For Fixed Sized Window
        # self.setFixedHeight(400)
        # self.setFixedWidth(300)
    # For Window Opacity
        #self.setWindowOpacity(0.8)
    # For Back Ground Color
        #self.setStyleSheet('background-color:green')
        self.Create_push_button()

    def Create_push_button(self): 
        btn1=QPushButton("Click",self)
       # btn1.move(200,200)
        btn1.setGeometry(100,100,100,100)
        # Change the icon of the Push Button
        btn1.setIcon(QIcon("python.png"))
        # Setting the text of the Button
        btn1.setText("CLICK-1")
        # Setting the Color of the Text
        btn1.setStyleSheet('color:red')
        # Setting the background Color of the Button

        btn1.setStyleSheet('background-color:Green')
    

        btn2=QPushButton("Click-2",self)
        btn2.setGeometry(200,100,100,100)
        btn2.setStyleSheet('color:green')
        btn2.setStyleSheet('background-color:Red')



app=QApplication(sys.argv)
window=WindowExample()
window.show()

sys.exit(app.exec_())