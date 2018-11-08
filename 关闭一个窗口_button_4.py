'''
关闭一个窗口
最明显的关闭一个窗口是点击标题栏上的x.在下个例子中,
我们会显示如何以编程的方式去关闭我们的窗口.
我们会接触一点信号和槽.

下面是一个QPushButton部件构造器,我们会用在例子中.
QPushButton(string text, QWidget parent = None)  
'''
import sys  
from PyQt5.QtWidgets import QWidget, QPushButton, QApplication  
from PyQt5.QtCore import QCoreApplication   
#我们需要来自QtCore模块的对象.
class Example(QWidget):   
    def __init__(self):  
        super().__init__()     
        self.initUI()  
  
    def initUI(self):                 
        qbtn = QPushButton('Quit', self)
        #  我们创建一个按钮.按钮是QPushButton类的一个实例.
        # 构造器的第一个参数是按钮的标签,第二个参数是父部件类.
        # 父部件是Example部件,是从QWidget继承来的.
        qbtn.clicked.connect(QCoreApplication.instance().quit)
        #在PyQt5中的事件处理系统是用信号和槽机制构建起来的.
        # 如果我们点击按钮,点击信号就会发出.槽可以是一个Qt槽或
        # 任何Python可调用的.QCoreApplication包含了主要的事件循环;
        # 它处理并分派所有事件.instance()方法给我们它当前的实例.
        # 注意QCoreApplication是用QApplication创建的.点击信息
        # 被连接到quit()方法,它会终止程序.通信是在发送者和接收者
        # 这两个对象之间完成的.这里的发送者是点击按钮,接收者是程序对象.  
        qbtn.resize(qbtn.sizeHint())  
        qbtn.move(50, 50)          
        self.setGeometry(300, 300, 250, 150)  
        self.setWindowTitle('Quit button')      
        self.show()   
          
if __name__ == '__main__':   
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())  