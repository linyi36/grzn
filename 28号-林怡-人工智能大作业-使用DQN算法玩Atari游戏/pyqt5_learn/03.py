from PyQt5.QtWidgets import *
app = QApplication([])
app.setStyle("Fusion")
button = QPushButton('Click') # 定义一个按钮

def on_button_clicked(): #定义一个事件
    alert = QMessageBox() #弹出一个消息框
    alert.setText('You clicked the button!') # 设定消息框文本
    alert.exec_() # 控制权交给它直到...

button.clicked.connect(on_button_clicked) #按钮和事件进行绑定
button.show() #展示控件
app.exec_()