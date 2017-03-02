# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'mainwindow.ui'
#
# Created by: PyQt5 UI code generator 5.7
#
# WARNING! All changes made in this file will be lost!

from PyQt5 import QtCore, QtGui, QtWidgets

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(750, 543)
        self.centralWidget = QtWidgets.QWidget(MainWindow)
        self.centralWidget.setObjectName("centralWidget")
        self.tabWidget = QtWidgets.QTabWidget(self.centralWidget)
        self.tabWidget.setGeometry(QtCore.QRect(0, 0, 751, 521))
        self.tabWidget.setObjectName("tabWidget")
        self.CPU_infor = QtWidgets.QWidget()
        self.CPU_infor.setObjectName("CPU_infor")
        self.gridLayoutWidget = QtWidgets.QWidget(self.CPU_infor)
        self.gridLayoutWidget.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.gridLayoutWidget.setObjectName("gridLayoutWidget")
        self.cpu_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget)
        self.cpu_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.cpu_gridLayout.setSpacing(6)
        self.cpu_gridLayout.setObjectName("cpu_gridLayout")
        self.tabWidget.addTab(self.CPU_infor, "")
        self.Mem_infor = QtWidgets.QWidget()
        self.Mem_infor.setObjectName("Mem_infor")
        self.gridLayoutWidget_2 = QtWidgets.QWidget(self.Mem_infor)
        self.gridLayoutWidget_2.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.gridLayoutWidget_2.setObjectName("gridLayoutWidget_2")
        self.mem_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_2)
        self.mem_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.mem_gridLayout.setSpacing(6)
        self.mem_gridLayout.setObjectName("mem_gridLayout")
        self.tabWidget.addTab(self.Mem_infor, "")
        self.Net_infor = QtWidgets.QWidget()
        self.Net_infor.setObjectName("Net_infor")
        self.gridLayoutWidget_3 = QtWidgets.QWidget(self.Net_infor)
        self.gridLayoutWidget_3.setGeometry(QtCore.QRect(0, 0, 741, 491))
        self.gridLayoutWidget_3.setObjectName("gridLayoutWidget_3")
        self.net_gridLayout = QtWidgets.QGridLayout(self.gridLayoutWidget_3)
        self.net_gridLayout.setContentsMargins(11, 11, 11, 11)
        self.net_gridLayout.setSpacing(6)
        self.net_gridLayout.setObjectName("net_gridLayout")
        self.tabWidget.addTab(self.Net_infor, "")
        self.Process_infor = QtWidgets.QWidget()
        self.Process_infor.setObjectName("Process_infor")
        self.pushButton = QtWidgets.QPushButton(self.Process_infor)
        self.pushButton.setGeometry(QtCore.QRect(0, 460, 113, 31))
        self.pushButton.setObjectName("pushButton")
        self.tableWidget = QtWidgets.QTableWidget(self.Process_infor)
        self.tableWidget.setGeometry(QtCore.QRect(0, 0, 761, 461))
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setColumnCount(6)
        self.tableWidget.setRowCount(0)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, item)
        item = QtWidgets.QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, item)
        self.tabWidget.addTab(self.Process_infor, "")
        MainWindow.setCentralWidget(self.centralWidget)
        self.menuBar = QtWidgets.QMenuBar(MainWindow)
        self.menuBar.setGeometry(QtCore.QRect(0, 0, 750, 22))
        self.menuBar.setObjectName("menuBar")
        self.menu = QtWidgets.QMenu(self.menuBar)
        self.menu.setObjectName("menu")
        MainWindow.setMenuBar(self.menuBar)
        self.actionCPU = QtWidgets.QAction(MainWindow)
        self.actionCPU.setObjectName("actionCPU")
        self.actionMem = QtWidgets.QAction(MainWindow)
        self.actionMem.setObjectName("actionMem")
        self.actionProcess = QtWidgets.QAction(MainWindow)
        self.actionProcess.setObjectName("actionProcess")
        self.actionExit = QtWidgets.QAction(MainWindow)
        self.actionExit.setObjectName("actionExit")
        self.menu.addAction(self.actionExit)
        self.menuBar.addAction(self.menu.menuAction())

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(3)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "资源管理器"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.CPU_infor), _translate("MainWindow", "CPU"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Mem_infor), _translate("MainWindow", "内存"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Net_infor), _translate("MainWindow", "网络"))
        self.pushButton.setText(_translate("MainWindow", "结束进程"))
        item = self.tableWidget.horizontalHeaderItem(0)
        item.setText(_translate("MainWindow", "PID"))
        item = self.tableWidget.horizontalHeaderItem(1)
        item.setText(_translate("MainWindow", "名称"))
        item = self.tableWidget.horizontalHeaderItem(2)
        item.setText(_translate("MainWindow", "状态"))
        item = self.tableWidget.horizontalHeaderItem(3)
        item.setText(_translate("MainWindow", "内存"))
        item = self.tableWidget.horizontalHeaderItem(4)
        item.setText(_translate("MainWindow", "线程数"))
        item = self.tableWidget.horizontalHeaderItem(5)
        item.setText(_translate("MainWindow", "用户"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Process_infor), _translate("MainWindow", "进程"))
        self.menu.setTitle(_translate("MainWindow", "菜单"))
        self.actionCPU.setText(_translate("MainWindow", "CPU"))
        self.actionMem.setText(_translate("MainWindow", "Mem"))
        self.actionProcess.setText(_translate("MainWindow", "Process"))
        self.actionExit.setText(_translate("MainWindow", "Exit"))

