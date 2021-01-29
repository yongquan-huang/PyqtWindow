# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'historyWin4.ui'
#
# Created by: PyQt5 UI code generator 5.15.1
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt5 import QtCore, QtGui, QtWidgets
from PyQt5.QtWidgets import QApplication,QWidget,QSizePolicy
import sys
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.pyplot as plt
import random
from PyQt5.QtGui import *
from PyQt5.QtCore import Qt
import re
import matplotlib.dates as md
from datetime import datetime
import matplotlib.ticker as ticker
import dateutil

class history_data(QWidget):
    def __init__(self):
        super(history_data,self).__init__()
        self.setupUi(self)
        self.MatplotlibWidget()

    def setupUi(self, history_data):
        history_data.setObjectName("history_data")
        history_data.resize(1400, 756)
        font = QtGui.QFont()
        font.setFamily("Agency FB")
        font.setPointSize(10)
        history_data.setFont(font)
        self.label = QtWidgets.QLabel(history_data)
        self.label.setGeometry(QtCore.QRect(20, 60, 91, 21))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(14)
        self.label.setFont(font)
        self.label.setObjectName("label")
        self.groupBox = QtWidgets.QGroupBox(history_data)
        self.groupBox.setGeometry(QtCore.QRect(-10, 90, 1400, 550))
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.gridLayoutWidget = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(10, 20, 341, 220))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.gridLayout.setObjectName("gridLayout")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(360, 20, 341, 220))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.gridLayout_2.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(10, 270, 341, 220))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.gridLayout_5.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_5.setObjectName("gridLayout_3")
        self.gridLayoutWidget_4 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_4.setGeometry(QtCore.QRect(1060, 20, 341, 220))
        self.gridLayoutWidget_4.setObjectName("gridLayoutWidget_4")
        self.gridLayout_4 = QtWidgets.QGridLayout(self.gridLayoutWidget_4)
        self.gridLayout_4.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_4.setObjectName("gridLayout_4")
        self.gridLayoutWidget_5 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_5.setGeometry(QtCore.QRect(710, 270, 341, 220))
        self.gridLayoutWidget_5.setObjectName("gridLayoutWidget_5")
        self.gridLayout_7 = QtWidgets.QGridLayout(self.gridLayoutWidget_5)
        self.gridLayout_7.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_7.setObjectName("gridLayout_5")
        self.gridLayoutWidget_6 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_6.setGeometry(QtCore.QRect(1060, 270, 341, 220))
        self.gridLayoutWidget_6.setObjectName("gridLayoutWidget_6")
        self.gridLayout_8 = QtWidgets.QGridLayout(self.gridLayoutWidget_6)
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_8.setObjectName("gridLayout_6")
        self.label_2 = QtWidgets.QLabel(self.groupBox)
        self.label_2.setGeometry(QtCore.QRect(140, 246, 51, 20))
        self.label_2.setObjectName("label_2")
        self.label_3 = QtWidgets.QLabel(self.groupBox)
        self.label_3.setGeometry(QtCore.QRect(500, 240, 51, 31))
        self.label_3.setObjectName("label_3")
        self.gridLayoutWidget_7 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_7.setGeometry(QtCore.QRect(710, 20, 341, 220))
        self.gridLayoutWidget_7.setObjectName("gridLayoutWidget_7")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.gridLayoutWidget_7)
        self.gridLayout_3.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_3.setObjectName("gridLayout_8")
        self.label_4 = QtWidgets.QLabel(self.groupBox)
        self.label_4.setGeometry(QtCore.QRect(840, 240, 101, 31))
        self.label_4.setObjectName("label_4")
        self.label_5 = QtWidgets.QLabel(self.groupBox)
        self.label_5.setGeometry(QtCore.QRect(1160, 245, 221, 20))
        self.label_5.setObjectName("label_5")
        self.label_6 = QtWidgets.QLabel(self.groupBox)
        self.label_6.setGeometry(QtCore.QRect(90, 500, 211, 20))
        self.label_6.setObjectName("label_6")
        self.gridLayoutWidget_8 = QtWidgets.QWidget(self.groupBox)
        self.gridLayoutWidget_8.setGeometry(QtCore.QRect(360, 270, 341, 220))
        self.gridLayoutWidget_8.setObjectName("gridLayoutWidget_8")
        self.gridLayout_6 = QtWidgets.QGridLayout(self.gridLayoutWidget_8)
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.gridLayout_6.setObjectName("gridLayout_9")
        self.label_7 = QtWidgets.QLabel(self.groupBox)
        self.label_7.setGeometry(QtCore.QRect(450, 500, 211, 20))
        self.label_7.setObjectName("label_7")
        self.label_8 = QtWidgets.QLabel(self.groupBox)
        self.label_8.setGeometry(QtCore.QRect(800, 500, 201, 21))
        self.label_8.setObjectName("label_8")
        self.label_9 = QtWidgets.QLabel(self.groupBox)
        self.label_9.setGeometry(QtCore.QRect(1160, 500, 171, 21))
        self.label_9.setObjectName("label_9")
        self.layoutWidget = QtWidgets.QWidget(history_data)
        self.layoutWidget.setGeometry(QtCore.QRect(0, 0, 532, 37))
        self.layoutWidget.setObjectName("layoutWidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.layoutWidget)
        self.horizontalLayout.setContentsMargins(0, 0, 0, 0)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.pushButton = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton.setFont(font)
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout.addWidget(self.pushButton)
        self.pushButton_2 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_2.setFont(font)
        self.pushButton_2.setObjectName("pushButton_2")
        self.horizontalLayout.addWidget(self.pushButton_2)
        self.pushButton_3 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_3.setFont(font)
        self.pushButton_3.setObjectName("pushButton_3")
        self.horizontalLayout.addWidget(self.pushButton_3)
        self.pushButton_4 = QtWidgets.QPushButton(self.layoutWidget)
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(16)
        self.pushButton_4.setFont(font)
        self.pushButton_4.setObjectName("pushButton_4")
        self.horizontalLayout.addWidget(self.pushButton_4)
        self.comboBox = QtWidgets.QComboBox(history_data)
        self.comboBox.setGeometry(QtCore.QRect(120, 60, 151, 22))
        font = QtGui.QFont()
        font.setFamily("Arial")
        font.setPointSize(11)
        self.comboBox.setFont(font)
        self.comboBox.setObjectName("comboBox")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")

        self.retranslateUi(history_data)
        QtCore.QMetaObject.connectSlotsByName(history_data)

    def retranslateUi(self, history_data):
        _translate = QtCore.QCoreApplication.translate
        history_data.setWindowTitle(_translate("history_data", "历史数据"))
        self.label.setText(_translate("history_data", "文件选择："))
        self.label_2.setText(_translate("history_data", "水温"))
        self.label_3.setText(_translate("history_data", "油压"))
        self.label_4.setText(_translate("history_data", "发动机转速"))
        self.label_5.setText(_translate("history_data", "作业部件流量"))
        self.label_6.setText(_translate("history_data", "输送辊马达压力"))
        self.label_7.setText(_translate("history_data", "切断刀马达压力"))
        self.label_8.setText(_translate("history_data", "排风机马达压力"))
        self.label_9.setText(_translate("history_data", "二级输送通道压力"))
        self.pushButton.setText(_translate("history_data", "实时数据"))
        self.pushButton_2.setText(_translate("history_data", "实时数据波形显示"))
        self.pushButton_3.setText(_translate("history_data", "历史数据"))
        self.pushButton_4.setText(_translate("history_data", "文件管理"))
        self.comboBox.setItemText(0, _translate("history_data", "文件1"))
        self.comboBox.setItemText(1, _translate("history_data", "文件2"))
        self.comboBox.setItemText(2, _translate("history_data", "文件3"))
        self.comboBox.setItemText(3, _translate("history_data", "文件4"))

    # def paintEvent(self, e):  #绘制曲线图各文字所对应的线
    #     qp = QPainter()
    #     qp.begin(self)
    #     # 水温红色
    #     pen = QPen(Qt.red, 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(170,326,184,326)
    #     # 油压橙色
    #     pen.setColor(QColor(245, 154,35))
    #     pen.setStyle(Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(530, 326, 544, 326)
    #     # 发动机转速黄色
    #     pen = QPen(Qt.yellow, 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(910, 326, 924, 326)
    #     # # 根切器马达黑色
    #     pen = QPen(Qt.black, 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(1247, 326, 1261, 326)
    #     pen = QPen(Qt.gray, 1, Qt.DashLine)
    #     qp.setPen(pen)
    #     qp.drawLine(1290, 326, 1304, 326)
    #     # 输送辊马达蓝色
    #     pen = QPen(Qt.blue, 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(177, 550, 191, 550)
    #     pen = QPen(QColor(129,211,248), 1, Qt.DashLine)
    #     qp.setPen(pen)
    #     qp.drawLine(220, 550, 234, 550)
    #     # 切断刀马达绿色
    #     pen = QPen(QColor(75, 121, 2), 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(536, 550, 550, 550)
    #     pen = QPen(QColor(202, 249, 130), 1, Qt.DashLine)
    #     qp.setPen(pen)
    #     qp.drawLine(580, 550, 594, 550)
    #     # 排风机马达粉色
    #     pen = QPen(QColor(240, 12, 203), 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(887, 550, 901, 550)
    #     pen = QPen(QColor(255, 192, 203), 1, Qt.DashLine)
    #     qp.setPen(pen)
    #     qp.drawLine(930, 550, 944, 550)
    #     # 二级输送通道马达棕色
    #     pen = QPen(QColor(165, 42, 42), 1, Qt.SolidLine)
    #     qp.setPen(pen)
    #     qp.drawLine(1259, 550, 1273, 550)
    #     pen = QPen(QColor(205, 133, 63), 1, Qt.DashLine)
    #     qp.setPen(pen)
    #     qp.drawLine(1303, 550, 1317, 550)
    #
    #     qp.end()

    def MatplotlibWidget(self):
        time_x1 = []
        time_x2 = []
        shuiwen_y = []
        youya_y = []
        fadongji_y = []
        genqieqiyali_1_y = []
        genqieqiyali_2_y = []
        genqieqiliuliang_y = []
        shusonggunyali_1_y = []
        shusonggunyali_2_y = []
        shusonggunliuliang_y = []
        qieduandaoyali_1_y = []
        qieduandaoyali_2_y = []
        qieduandaoliuliang_y = []
        paifengjiyali_1_y = []
        paifengjiyali_2_y = []
        paifengjiliuliang_y = []
        erjishusongyali_1_y = []
        erjishusongyali_2_y = []
        erjishusongliuliang_y = []

        # 读取扭矩或者是5个传感器压力
        # with open(r'E:\甘蔗机网关\cane11.6\run\run2020\env2019\env\torque_data.txt') as f:
        with open('/home/rpdzkj/run/run2020/env2019/env/ins_data.txt') as f:
            line = f.readline()
            while line:
                ins_data = eval(line)
                time_x1.append(ins_data['time'])
                shuiwen_y.append(ins_data['water_temperature'])
                youya_y.append(ins_data['oil_pressure'])
                fadongji_y.append(ins_data['engine_speed'])
                qieduandaoyali_1_y.append(ins_data['fluid_one'])
                qieduandaoyali_2_y.append(ins_data['fluid_two'])
                paifengjiyali_1_y.append(ins_data['fluid_three'])
                paifengjiyali_2_y.append(ins_data['fluid_four'])
                shusonggunyali_1_y.append(ins_data['fluid_five'])
                shusonggunyali_2_y.append(ins_data['fluid_six'])
                erjishusongyali_1_y.append(ins_data['fluid_senven'])
                erjishusongyali_2_y.append(ins_data['fluid_eight'])
                line = f.readline()
        # 读取仪表盘数据：转速，水温，油压
        # with open(r'E:\甘蔗机网关\cane11.6\run\run2020\env2019\env\ins_data.txt') as f:
        # 读取5个传感器流量
        with open('/home/rpdzkj/run/run2020/env2019/env/flow_data.txt') as f:
            line2 = f.readline()
            while line2:
                flow_data = eval(line2)
                time_x2.append(flow_data['time'])
                # time_x2.append((ins_data['time']))
                qieduandaoliuliang_y.append(flow_data['flow_one'])
                paifengjiliuliang_y.append(flow_data['flow_two'])
                shusonggunliuliang_y.append(flow_data['flow_three'])
                erjishusongliuliang_y.append(flow_data['flow_four'])
                line2 = f.readline()

        # 水温图
        self.shuiwen = History_Canvas()
        # self.shuiwen.history_plot()
        # x = [i for i in range(1,11)]  模拟数据
        # y1 = [random.randint(0, 100) for i in range(10)]
        self.shuiwen.shuiwen_line(time_x1, shuiwen_y)
        self.gridLayout.addWidget(self.shuiwen)
        # 油压图
        self.youya = History_Canvas()
        # self.youya.history_plot()
        # x = [i for i in range(1, 11)]
        # y2 = [random.randint(0, 100) for i in range(10)]
        self.youya.youya_line(time_x1, youya_y)
        self.gridLayout_2.addWidget(self.youya)
        # 发动机转速
        self.fadongji = History_Canvas()
        # self.fadongji.history_plot()
        # x = [i for i in range(1, 11)]
        # y3 = [random.randint(0, 100) for i in range(10)]
        self.fadongji.fadongji_line(time_x1, fadongji_y)
        self.gridLayout_3.addWidget(self.fadongji)
        # 作业部件流量   （根切器马达）
        self.liuliang = History_Canvas()
        # self.genqieqi.history_plot()
        # x = [i for i in range(1, 11)]
        # y4 = [random.randint(0, 100) for i in range(10)]
        # y5 = [random.randint(0, 100) for i in range(10)]
        self.liuliang.liuliang_line(time_x2, shusonggunliuliang_y, qieduandaoliuliang_y, paifengjiliuliang_y, erjishusongliuliang_y)
        self.gridLayout_4.addWidget(self.liuliang)
        # 输送辊马达压力
        self.shusonggun = History_Canvas()
        # self.shusonggun.history_plot()
        # # x = [i for i in range(1, 11)]
        # # y6 = [random.randint(0, 100) for i in range(10)]
        # # y7 = [random.randint(0, 100) for i in range(10)]
        self.shusonggun.shusonggun_line(time_x1, shusonggunyali_1_y, shusonggunyali_2_y)
        self.gridLayout_5.addWidget(self.shusonggun)
        # # 切断刀马达压力
        self.qieduandao = History_Canvas()
        # self.qieduandao.history_plot()
        # # x = [i for i in range(1, 11)]
        # # y8 = [random.randint(0, 100) for i in range(10)]
        # # y9 = [random.randint(0, 100) for i in range(10)]
        self.qieduandao.qieduandao_line(time_x1, qieduandaoyali_1_y, qieduandaoyali_2_y)
        self.gridLayout_6.addWidget(self.qieduandao)
        # # 排风机马达压力
        self.paifengji = History_Canvas()
        # self.paifengji.history_plot()
        # # x = [i for i in range(1, 11)]
        # # y10 = [random.randint(0, 100) for i in range(10)]
        # # y11 = [random.randint(0, 100) for i in range(10)]
        self.paifengji.paifengji_line(time_x1, paifengjiyali_1_y, paifengjiyali_2_y)
        self.gridLayout_7.addWidget(self.paifengji)
        # # 二级输送压力
        self.erjishusong = History_Canvas()
        # self.erjishusong.history_plot()
        # # x = [i for i in range(1, 11)]
        # # y10 = [random.randint(0, 100) for i in range(10)]
        # # y11 = [random.randint(0, 100) for i in range(10)]
        self.erjishusong.erjishusong_line(time_x1, erjishusongyali_1_y, erjishusongyali_2_y)
        self.gridLayout_8.addWidget(self.erjishusong)

class History_Canvas(FigureCanvas):  #画板
    def __init__(self, parent=None, width=8.56, height=3.83, dpi=100):      #dpi用来控制标签的字体大小
        # 配置中文显示
        plt.rcParams['font.family'] = ['SimHei']  # 用来正常显示中文标签
        plt.rcParams['axes.unicode_minus'] = False  # 用来正常显示负号
        # 新建一个绘图对象
        self.fig = Figure(figsize=(width,height), dpi=80)
        self.axes = self.fig.add_subplot(111)
        self.fig.autofmt_xdate()  #自动旋转横坐标标签
        super(History_Canvas, self).__init__(self.fig)
        '''定义FigureCanvas的尺寸策略，这部分的意思是设置FigureCanvas，使之尽可能的向外填充空间。'''
        FigureCanvas.setSizePolicy(self, QSizePolicy.Expanding, QSizePolicy.Expanding)
        FigureCanvas.updateGeometry(self)

    def history_plot(self):
        #设置坐标轴的标签
        self.axes.set_xlabel('X轴：时间')
        self.axes.set_ylabel('Y轴：值')

    def shuiwen_line(self,x,y1):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')   # 设置x轴刻度表示
        self.axes.xaxis.set_major_formatter(xfmt)
        tick_spacing = 10
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))   #设置y轴刻度的间隔
        self.axes.plot(x, y1, color='red')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 图例左上角
    def youya_line(self,x,y2):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        tick_spacing = 10
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))  # 设置y轴刻度的间隔
        self.axes.plot(x, y2, color='orange')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
    def fadongji_line(self,x,y3):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        tick_spacing = 10
        self.axes.yaxis.set_major_locator(ticker.MultipleLocator(tick_spacing))  # 设置y轴刻度的间隔
        self.axes.plot(x, y3, color='yellow')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
    def liuliang_line(self,x,y4_1,y4_2,y4_3,y4_4):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  #格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        self.axes.plot(x, y4_1, color='#81D3F8', linestyle='--', label='一级输送流量')
        self.axes.plot(x, y4_2, color='#CAF982', linestyle='--', label='切段刀流量')
        self.axes.plot(x, y4_3, color='#FFC0CB', linestyle='--', label='除杂风机流量')
        self.axes.plot(x, y4_4, color='#CD853F', linestyle='--', label='二级输送流量')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
    def shusonggun_line(self,x,y6_1,y6_2):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        self.axes.plot(x, y6_1, color='#81D3F8', label='压力1')
        self.axes.plot(x, y6_2, color='blue', label='压力2')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
        # self.axes.plot(x, y7, color='#81D3F8',linestyle='--')
        # self.axes.grid(True)
    def qieduandao_line(self,x,y8_1,y8_2):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        self.axes.plot(x, y8_1, color='#CAF982', label='压力1')
        self.axes.plot(x, y8_2, color='#4B7902', label='压力2')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
        # self.axes.plot(x, y9, color='#CAF982',linestyle='--')
        # self.axes.grid(True)
    def paifengji_line(self,x,y10_1,y10_2):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        self.axes.plot(x, y10_1, color='#FFC0CB', label='压力1')
        self.axes.plot(x, y10_2, color='#F00CCB', label='压力2')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
        # self.axes.plot(x, y11, color='#FFC0CB',linestyle='--')
        # self.axes.grid(True)
    def erjishusong_line(self,x,y12_1,y12_2):
        x = [datetime.strptime(d, '%d-%H-%M-%S') for d in x]  # 格式化字符串
        xfmt = md.DateFormatter('%d %H:%M:%S')
        self.axes.xaxis.set_major_formatter(xfmt)
        self.axes.plot(x, y12_1, color='#CD853F', label='压力1')
        self.axes.plot(x, y12_2, color='#A52A2A', label='压力2')
        self.axes.grid(True)
        self.axes.legend(loc='upper left')  # 左上角
        # self.axes.plot(x, y13, color='#CD853F',linestyle='--')
        # self.axes.grid(True)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    w = history_data()
    w.show()
    sys.exit(app.exec_())