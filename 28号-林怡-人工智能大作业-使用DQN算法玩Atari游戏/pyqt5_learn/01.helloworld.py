from PyQt5 import QtWidgets #https://doc.qt.io/qt-5/qtwidgets-index.html
from PyQt5.QtWidgets import QApplication,QMainWindow
import sys

class MyWindow(QMainWindow):
    def __init__(self):
        super(MyWindow,self).__init__();
        self.setGeometry(500,300,400,400)  # 两点确定一个window(左上和右下)
        self.setWindowTitle("title ss")
        self.initUI()

    def initUI(self):
        self.label = QtWidgets.QLabel(self)  # 指定是哪个对象的标签!
        self.label.setText("Date:!")
        self.label.move(59, 100)

        self.b1 = QtWidgets.QPushButton(self)
        self.b1.setText("Click me")
        self.b1.clicked.connect(self.clicked)  # b1的点击事件绑定一个函数

    def clicked(self):
        self.label.setText("you pressed the button")
        self.update()

    def update(self):
        self.label.adjustSize()


def window():
    app=QApplication(sys.argv) #???
    win=MyWindow()
    win.show()
    sys.exit(app.exec_())  #???

window()