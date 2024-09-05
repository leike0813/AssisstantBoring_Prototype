import datetime
import sys, os
import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC, PySide2.QtGui as QtG
import numpy as np
import pandas as pd
import qtawesome as qta
from globals import GlobalContainer as GC
from widgets.daemonWidget import DaemonWidget
from pyside2_utils.widgets import QIPythonConsoleWidget
from ui.Ui_MainWindow import Ui_MainWindow
from widgets.mdiSubWidgets import *


class MainWindow(QtW.QMainWindow, Ui_MainWindow):
    '''
    辅助掘进系统主窗口。
    '''
    def __init__(self, config):
        super(MainWindow, self).__init__()
        # 初始化UI（Designer规定动作）
        self.setupUi(self)
        # 初始化参数
        self.config = config
        self.__currentStatusBarPriority = 0

        # 初始化状态栏的连接
        self.statusBar().messageChanged.connect(self.resetStatusBarPriority)
        # 初始化MDI区域
        self.initializeMDIArea()
        # 调整UI
        self.adjustUi()
        # 初始化后台监控控件
        self.daemonWidget = DaemonWidget(self)

        # 初始化控制台
        if not self.config.DEBUG.disableConsole:
            self.initConsole()

    def initializeMDIArea(self):
        # 初始化MDI子窗口
        self.monitor_SubWidget = Monitor_SubWidget()
        self.muckAnalysis_SubWidget = MuckAnalysis_SubWidget()
        self.vibrationAnalysis_SubWidget = VibrationAnalysis_SubWidget()
        self.query_SubWidget = Query_SubWidget()
        # 将MDI子窗口添加到MDI区域
        self.mdiArea.addSubWindow(self.monitor_SubWidget)
        self.mdiArea.addSubWindow(self.muckAnalysis_SubWidget)
        self.mdiArea.addSubWindow(self.vibrationAnalysis_SubWidget)
        self.mdiArea.addSubWindow(self.query_SubWidget)
        # 将MDIArea的子窗体赋值给属性，方便调用
        self.monitor_SubWindow = self.mdiArea.subWindowList()[0]
        self.muckAnalysis_SubWindow = self.mdiArea.subWindowList()[1]
        self.vibrationAnalysis_SubWindow = self.mdiArea.subWindowList()[2]
        self.query_SubWindow = self.mdiArea.subWindowList()[3]

    def adjustUi(self):
        self.__developing_apps = [
            self.action_VibrationAnalysis_App,
            self.action_Optimization_App,
        ]

        # 定义窗口按钮相关映射字典
        self.action_Mapper = {
            self.monitor_SubWindow: self.action_Monitor_App,
            self.muckAnalysis_SubWindow: self.action_MuckAnalysis_App,
            self.vibrationAnalysis_SubWindow: self.action_VibrationAnalysis_App,
            self.query_SubWindow: self.action_Query_App
        }
        self.subWindow_Mapper = {
            list(self.action_Mapper.values())[i]:
                list(self.action_Mapper.keys())[i] for i in range(len(self.action_Mapper))
        }
        self.iconString_Mapper = {
            self.action_Monitor_App: 'mdi6.gauge',
            self.action_MuckAnalysis_App: 'mdi6.camera',
            self.action_VibrationAnalysis_App: 'mdi6.sine-wave',
            self.action_Optimization_App: 'mdi6.lightning-bolt-circle',
            self.action_Query_App: 'mdi6.database-search',
            self.action_Console: 'mdi6.console',
            self.action_Help: 'mdi6.help',
            self.action_Logout: 'mdi6.exit-run'
        }
        # 初始化toolbar和图标
        self.toolBar.insertSeparator(self.action_Console)
        self.toolBar_IconScale = 0.66
        # 设置toolbar字体，14号幼圆
        font = QtG.QFont()
        font.setFamily(u"\u5e7c\u5706")
        font.setPointSize(14)
        font.setBold(True)
        font.setWeight(75)
        self.toolBar.setFont(font)
        # 设置toolbar图标
        for k, v in self.iconString_Mapper.items():
            k.setIcon(qta.icon(v, color = 'deepskyblue', scale_factor = self.toolBar_IconScale))
        self.toolBar.setToolButtonStyle(QtC.Qt.ToolButtonTextUnderIcon)
        # 初始化mdi子窗口状态
        self.monitor_SubWindow.setWindowState(self.monitor_SubWindow.windowState() ^ QtC.Qt.WindowMaximized)
        self.muckAnalysis_SubWindow.hide()
        self.vibrationAnalysis_SubWindow.hide()
        self.query_SubWindow.hide()
        # 设置mdi区域滚动条规则
        self.mdiArea.setHorizontalScrollBarPolicy(QtC.Qt.ScrollBarAsNeeded)
        self.mdiArea.setVerticalScrollBarPolicy(QtC.Qt.ScrollBarAsNeeded)
        # 为自己安装eventFilter,重定向closeEvent
        self.installEventFilter(self)
        # 设置mdi子窗口，安装eventFilter重定向其closeEvent，将对应的按钮连接至统一处理函数
        self.monitor_SubWindow.installEventFilter(self)
        self.action_Monitor_App.toggled.connect(self.onActionToggled) # 按钮连接
        self.muckAnalysis_SubWindow.installEventFilter(self)
        self.action_MuckAnalysis_App.toggled.connect(self.onActionToggled) # 按钮连接
        self.vibrationAnalysis_SubWindow.installEventFilter(self)
        self.action_VibrationAnalysis_App.toggled.connect(self.onActionToggled) # 按钮连接
        self.action_Optimization_App.toggled.connect(self.onActionToggled) # 按钮连接
        self.query_SubWindow.installEventFilter(self)
        self.action_Query_App.toggled.connect(self.onActionToggled) # 按钮连接
        self.mdiArea.subWindowActivated.connect(self.onSubWindowActivated) # 实现焦点窗口图标变色
        # self.action_Logout.triggered.connect(self.close) # logout定向至主窗口关闭
        self.action_Monitor_App.setChecked(True)

    def eventFilter(self, watched, event):
        # 重定向自身的关闭事件，先关闭后台线程和所有子窗口，再退回登录窗口
        if event.type() == QtC.QEvent.Close:
            if watched is self:
                status = QtW.QMessageBox.question(self, '确认', '确定要退出TBM智能辅助掘进系统？')
                if status == QtW.QMessageBox.Yes:
                    event.accept()
                    self.daemonWidget.close()
                    if not self.config.DEBUG.disableConsole:
                        self.console.close()
                else:
                    event.ignore()
                return True
            # 重定向MDI子窗口的关闭事件，改由响应按钮弹起事件的处理函数接手
            elif watched in self.action_Mapper.keys():
                event.ignore()
                self.action_Mapper[watched].setChecked(False)
                return True
            elif watched is self.console:
                event.ignore()
                self.action_Console.setChecked(False)
                return True
        elif event.type() == QtC.QEvent.Show:
            if watched is self:
                if self.config.UI.SHOW_DAEMON:
                    self.daemonWidget.show()
                self.show()
                return True
        # MDI子窗体最小化事件，令其改变图标颜色
        elif event.type() == QtC.QEvent.WindowStateChange and watched.isMinimized():
            if watched in self.action_Mapper.keys():
                self.action_Mapper[watched].setIcon(
                    qta.icon(self.iconString_Mapper[self.action_Mapper[watched]],
                             color = 'deepskyblue', scale_factor = self.toolBar_IconScale))
                event.accept()
                return super(MainWindow, self).eventFilter(watched, event)
        return super(MainWindow, self).eventFilter(watched, event)

    @QtC.Slot(str, int, int)
    def statusBarShowMessage(self, str, timeout, priority):
        if priority >= self.__currentStatusBarPriority:
            self.statusBar().showMessage(str, timeout)
            self.__currentStatusBarPriority = priority

    @QtC.Slot()
    def resetStatusBarPriority(self):
        self.__currentStatusBarPriority = 0

    @QtC.Slot(QtC.QObject)
    def onSubWindowActivated(self, subWindow):
        if subWindow:
            action = self.action_Mapper[subWindow]
            if not subWindow.isMinimized(): # 焦点切换至最小化的窗口时图标不变色
                action.setIcon(qta.icon(self.iconString_Mapper[action], color = 'gold',
                                        scale_factor = self.toolBar_IconScale))
            for k, v in self.action_Mapper.items():
                if k is not subWindow:
                    v.setIcon(qta.icon(self.iconString_Mapper[v], color = 'deepskyblue',
                                       scale_factor = self.toolBar_IconScale))

    @QtC.Slot(bool)
    def onActionToggled(self, triggered):
        action = self.sender()

        if action in self.__developing_apps:
            if action.isChecked():
                QtW.QMessageBox.information(self, '提示', '正在开发中，敬请期待。', QtW.QMessageBox.Ok)
                action.setChecked(False)
            return

        subWindow = self.subWindow_Mapper[action]
        iconString = self.iconString_Mapper[action]
        if triggered: # 按钮未按下，则按下按钮，显示窗口并置于焦点
            subWindow.show()
            # action.setIcon(qta.icon(iconString, color = 'gold', scale_factor = 0.5))
        else: # 按钮已按下，代表窗口已以某种形式打开
            if self.mdiArea.activeSubWindow() is subWindow: # 窗口为当前焦点
                if subWindow.isMinimized(): # 窗口为当前焦点，但被最小化
                    subWindow.setWindowState(subWindow.windowState() ^ QtC.Qt.WindowMinimized) # 还原窗口
                    action.setChecked(True) # 使按钮保持按下
                    self.mdiArea.subWindowActivated.emit(subWindow) # 发出焦点转移信号，强制图标变色
                else:# 窗口为当前焦点且未被最小化，此时按下按钮为关闭窗口
                    subWindow.hide()
                    action.setIcon(qta.icon(iconString, color = 'deepskyblue',
                                            scale_factor = self.toolBar_IconScale))
            else:# 窗口不是当前焦点
                if subWindow.isMinimized(): # 窗口不是当前焦点，但被最小化
                    subWindow.setWindowState(subWindow.windowState() ^ QtC.Qt.WindowMinimized)  # 还原窗口
                    self.mdiArea.subWindowActivated.emit(subWindow)  # 发出焦点转移信号，强制图标变色
                self.mdiArea.setActiveSubWindow(subWindow) # 使窗口成为焦点
                action.setChecked(True) # 使按钮保持按下

    @QtC.Slot(bool)
    def on_action_Console_triggered(self, triggered):
        if triggered:
            if self.config.DEBUG.disableConsole:
                status = QtW.QMessageBox.critical(self, '错误', '控制台已被禁用。', QtW.QMessageBox.Ok)
                self.action_Console.setChecked(False)
            else:
                self.console.show()
        else:
            self.console.hide()

    @QtC.Slot(bool)
    def on_action_Logout_triggered(self, triggered):
        self.daemonWidget.hide()
        if not self.config.DEBUG.disableConsole:
            self.console.hide()
        self.hide()
        GC.loginWindow.show()

    def initConsole(self):
        """
        初始化调试控制台。
        """
        self.console = QIPythonConsoleWidget(self, self)
        self.console.push({"sys": sys, "os": os, "QtC": QtC, "QtW": QtW, "QtG": QtG, "np": np, "pd": pd})

