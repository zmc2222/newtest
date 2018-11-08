'''
一个应用图标
一个应用图标是一个用于显示在标题栏最左上角的小图像.
在下面的例子中我们会在PyQt5中演示,
同时我们还会介绍一个新的方法.
'''
import sys  
from PyQt5.QtWidgets import QApplication, QWidget  
from PyQt5.QtGui import QIcon         
class Example(QWidget):      
    def __init__(self):  
        super().__init__()     
        self.initUI()

    def initUI(self):        
        self.setGeometry(300, 300, 300, 220)
        #相当于move  和 resize 方法合并  
        self.setWindowTitle('Icon')  
        self.setWindowIcon(QIcon('/home/tarena/下载/bbb'))          
        #QIcon("图片路径"")生成一个图标对象，然后被
        #传入文件路径无效并不会报错
        #setWindowIcon方法生成显示程序
        self.show()  
              
if __name__ == '__main__':     
        
    app = QApplication(sys.argv)  
    ex = Example()  
    sys.exit(app.exec_())    