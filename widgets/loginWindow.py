import PySide2.QtWidgets as QtW, PySide2.QtCore as QtC
from globals import GlobalContainer as GC
from widgets.mainWindow import MainWindow
from ui.Ui_LoginWindow import Ui_LoginWindow
from config import DEFAULT_CONFIG

class LoginWindow(QtW.QWidget, Ui_LoginWindow):
    '''
    辅助掘进系统登录窗口。
    '''
    def __init__(self, config=DEFAULT_CONFIG.clone()):
        super(LoginWindow, self).__init__()
        self.setupUi(self)
        self.adjustUi()
        self.config = config

    def adjustUi(self):
        '''
        初始化高级选项折叠控件。
        '''
        self.collapseWidget.toggle_Button.setText(\
            QtC.QCoreApplication.translate("LoginWindow", u"\u9ad8\u7ea7\u9009\u9879", None)\
            )
        self.contentAreaLayout.setParent(None)
        self.collapseWidget.setContentLayout(self.contentAreaLayout)


    @QtC.Slot()
    def on_advance_ToolButton_pressed(self):
        '''高级选项按钮的触发槽'''
        checked = self.advance_ToolButton.isChecked()
        self.advance_ToolButton.setArrowType(QtC.Qt.DownArrow if not checked else QtC.Qt.RightArrow)


    @QtC.Slot()
    def on_username_LineEdit_returnPressed(self):
        '''将用户名控件的按下回车动作重定向到登录按钮的点击动作'''
        self.on_login_PushButton_clicked()

    @QtC.Slot()
    def on_password_LineEdit_returnPressed(self):
        '''将密码控件的按下回车动作重定向到登录按钮的点击动作'''
        self.on_login_PushButton_clicked()

    @QtC.Slot()
    def on_login_PushButton_clicked(self):
        '''登录按钮的触发槽'''
        # 获取控件中输入的用户名及密码
        username = self.username_LineEdit.text().strip()
        password = self.password_LineEdit.text().strip()

        if username not in self.config.AUTHORIZATION.USERS \
                or password != self.config.AUTHORIZATION.PASSWORDS[username]:
            QtW.QMessageBox.warning(self, '登陆失败', '用户名或密码错误！')
            return
        # 若ret为0，说明登录成功，打开主窗口并隐藏登录窗口
        if not GC.mainWindow: # 如果GlobalContainer中没有已创建的主窗口实例，则创建
            GC.mainWindow = MainWindow(self.config)
        GC.mainWindow.show()
        self.hide()