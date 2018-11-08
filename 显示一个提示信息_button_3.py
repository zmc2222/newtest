'''
pyqt5 project3
显示一个提示信息
我们可以为我们的任何一个窗体提供悬浮帮助信息.
'''
import sys   
from PyQt5.QtWidgets import (QWidget, QToolTip,\
QPushButton, QApplication)   
from PyQt5.QtGui import QFont             
class Example(QWidget):              
    def __init__(self):           
        super().__init__()                      
        self.initUI()                             
    def initUI(self):                      
        QToolTip.setFont(QFont('SansSerif', 10))
        #这个静态方法设置了一种字体用于绘制提示信息.
        # 我们使用了10像素的SansSerif字体.                      
        self.setToolTip('This is a <b>QWidget</b> widget')
        #要创建一个提示信息,我们要调用setTooltip()方法.
        # 我们可以直接用多格式文件来格式化它.                      
        btn = QPushButton('Button', self)           
        btn.setToolTip('This is a <b>QPushButton</b> widget')
        #我们创建一个点击按钮并给它设置一个提示信息.           
        btn.resize(btn.sizeHint())           
        btn.move(50, 50)
        #      这是用于把按钮定义大小和在窗体位置的.
        # sizeHint()方法会给按钮一个推荐的大小.                       
        self.setGeometry(300, 300, 300, 200)           
        self.setWindowTitle('Tooltips')               
        self.show()                         
    if __name__ == '__main__':              
        app = QApplication(sys.argv)       
        ex = Example()       
        sys.exit(app.exec_())