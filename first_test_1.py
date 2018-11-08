import sys
from PyQt5 import QtWidgets,QtCore
#这们在这里进行必要的导入.
# 基本的窗口集在PyQt5.QtWidgets模块里.

app = QtWidgets.QApplication(sys.argv)
#每一个PyQt5应用都必须创建一个应用对象
# .sys.argv参数是来自命令行的参数列表.
# Python脚本可以从shell里运行.这是我们如何控制
# 我们的脚本运行的一种方法.

widget = QtWidgets.QWidget()
#QWidget窗口是PyQt5中所有用户界口对象的基本类.
# 我们使用了QWidget默认的构造器.默认的构造器没有
# 父类.一个没有父类的窗口被称为一个window.

widget.resize(800,360)#（wetght,high）
#esize()方法调整了窗口的大小.
# 被调整为 w * h 像素高.

widget.move(100,100)
#move()方法移动窗口到屏幕坐标 x=300，y=300
#的位置
#具体坐标参数设定需要再细细测试，
# 或者向老师咨询算法问题
widget.setWindowTitle("hello,pyqt5")
# setWindowTitle是设置标题内容的函数

widget.show()
#show（）方法讲窗口显示到屏幕上。
sys.exit(app.exec_())