import sys
from PyQt5.QtWidgets import QApplication,QWidget,QDialog,QMainWindow
from PyQt5.QtGui import QIcon

# Three Types of Windows are there Qwidget,QDialog,QMainWindow 
class WindowExample(QMainWindow):
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
        self.setWindowOpacity(0.8)
    # For Back Ground Color
        self.setStyleSheet('background-color:green')
        self.show()

app=QApplication(sys.argv)
window=WindowExample()
sys.exit(app.exec_())