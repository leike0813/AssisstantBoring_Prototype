# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'Ui_MuckAnalysis_SubWidget.ui'
##
## Created by: Qt User Interface Compiler version 5.15.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide2.QtCore import *
from PySide2.QtGui import *
from PySide2.QtWidgets import *

from pyside2_utils.widgets import QMatplotlibWidget


class Ui_MuckAnalysis_SubWidget(object):
    def setupUi(self, MuckAnalysis_SubWidget):
        if not MuckAnalysis_SubWidget.objectName():
            MuckAnalysis_SubWidget.setObjectName(u"MuckAnalysis_SubWidget")
        MuckAnalysis_SubWidget.resize(1920, 1080)
        self.horizontalLayout = QHBoxLayout(MuckAnalysis_SubWidget)
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.groupBox_10 = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox_10.setObjectName(u"groupBox_10")
        font = QFont()
        font.setFamily(u"Microsoft YaHei UI")
        font.setPointSize(12)
        font.setBold(True)
        font.setWeight(75)
        self.groupBox_10.setFont(font)
        self.gridLayout = QGridLayout(self.groupBox_10)
        self.gridLayout.setObjectName(u"gridLayout")
        self.gridLayout.setContentsMargins(0, 0, 0, 0)
        self.label_26 = QLabel(self.groupBox_10)
        self.label_26.setObjectName(u"label_26")
        font1 = QFont()
        font1.setFamily(u"Microsoft YaHei UI")
        font1.setPointSize(12)
        font1.setBold(False)
        font1.setWeight(50)
        self.label_26.setFont(font1)

        self.gridLayout.addWidget(self.label_26, 0, 2, 1, 1)

        self.label_25 = QLabel(self.groupBox_10)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setFont(font1)

        self.gridLayout.addWidget(self.label_25, 0, 0, 1, 1)

        self.dateEdit = QDateEdit(self.groupBox_10)
        self.dateEdit.setObjectName(u"dateEdit")
        self.dateEdit.setFont(font1)
        self.dateEdit.setDateTime(QDateTime(QDate(2018, 6, 27), QTime(0, 0, 0)))

        self.gridLayout.addWidget(self.dateEdit, 0, 1, 1, 1)

        self.time_ComboBox = QComboBox(self.groupBox_10)
        self.time_ComboBox.addItem("")
        self.time_ComboBox.setObjectName(u"time_ComboBox")
        sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.time_ComboBox.sizePolicy().hasHeightForWidth())
        self.time_ComboBox.setSizePolicy(sizePolicy)
        self.time_ComboBox.setMaximumSize(QSize(16777215, 20))
        self.time_ComboBox.setFont(font1)
        self.time_ComboBox.setFrame(True)

        self.gridLayout.addWidget(self.time_ComboBox, 0, 3, 1, 1)


        self.verticalLayout.addWidget(self.groupBox_10)

        self.groupBox_11 = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox_11.setObjectName(u"groupBox_11")
        self.groupBox_11.setFont(font)
        self.gridLayout_6 = QGridLayout(self.groupBox_11)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.gridLayout_6.setContentsMargins(0, 0, 0, 0)
        self.label_41 = QLabel(self.groupBox_11)
        self.label_41.setObjectName(u"label_41")
        font2 = QFont()
        font2.setFamily(u"Times New Roman")
        font2.setPointSize(12)
        font2.setBold(False)
        font2.setWeight(50)
        self.label_41.setFont(font2)

        self.gridLayout_6.addWidget(self.label_41, 0, 0, 1, 1)

        self.t_LineEdit = QLineEdit(self.groupBox_11)
        self.t_LineEdit.setObjectName(u"t_LineEdit")
        self.t_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.t_LineEdit, 0, 7, 1, 1)

        self.label_38 = QLabel(self.groupBox_11)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font2)

        self.gridLayout_6.addWidget(self.label_38, 0, 8, 1, 1)

        self.f_LineEdit = QLineEdit(self.groupBox_11)
        self.f_LineEdit.setObjectName(u"f_LineEdit")
        self.f_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.f_LineEdit, 0, 3, 1, 1)

        self.vr_LineEdit = QLineEdit(self.groupBox_11)
        self.vr_LineEdit.setObjectName(u"vr_LineEdit")
        self.vr_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.vr_LineEdit, 0, 5, 1, 1)

        self.label_37 = QLabel(self.groupBox_11)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font2)

        self.gridLayout_6.addWidget(self.label_37, 0, 2, 1, 1)

        self.label_40 = QLabel(self.groupBox_11)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font2)

        self.gridLayout_6.addWidget(self.label_40, 0, 4, 1, 1)

        self.label_39 = QLabel(self.groupBox_11)
        self.label_39.setObjectName(u"label_39")
        self.label_39.setFont(font2)

        self.gridLayout_6.addWidget(self.label_39, 0, 6, 1, 1)

        self.pr_LineEdit = QLineEdit(self.groupBox_11)
        self.pr_LineEdit.setObjectName(u"pr_LineEdit")
        self.pr_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.pr_LineEdit, 0, 1, 1, 1)

        self.vp_LineEdit = QLineEdit(self.groupBox_11)
        self.vp_LineEdit.setObjectName(u"vp_LineEdit")
        self.vp_LineEdit.setReadOnly(True)

        self.gridLayout_6.addWidget(self.vp_LineEdit, 0, 9, 1, 1)

        self.gridLayout_6.setColumnStretch(0, 1)
        self.gridLayout_6.setColumnStretch(1, 1)
        self.gridLayout_6.setColumnStretch(2, 1)
        self.gridLayout_6.setColumnStretch(3, 1)
        self.gridLayout_6.setColumnStretch(4, 1)
        self.gridLayout_6.setColumnStretch(5, 1)
        self.gridLayout_6.setColumnStretch(6, 1)
        self.gridLayout_6.setColumnStretch(7, 1)
        self.gridLayout_6.setColumnStretch(8, 1)
        self.gridLayout_6.setColumnStretch(9, 1)

        self.verticalLayout.addWidget(self.groupBox_11)

        self.groupBox_13 = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox_13.setObjectName(u"groupBox_13")
        self.groupBox_13.setFont(font)
        self.gridLayout_9 = QGridLayout(self.groupBox_13)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.gridLayout_9.setContentsMargins(0, 0, 0, 0)
        self.vol_LineEdit = QLineEdit(self.groupBox_13)
        self.vol_LineEdit.setObjectName(u"vol_LineEdit")
        self.vol_LineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.vol_LineEdit, 0, 1, 1, 1)

        self.label_45 = QLabel(self.groupBox_13)
        self.label_45.setObjectName(u"label_45")
        self.label_45.setFont(font2)

        self.gridLayout_9.addWidget(self.label_45, 0, 4, 1, 1)

        self.cu_LineEdit = QLineEdit(self.groupBox_13)
        self.cu_LineEdit.setObjectName(u"cu_LineEdit")
        self.cu_LineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.cu_LineEdit, 0, 5, 1, 1)

        self.cc_LineEdit = QLineEdit(self.groupBox_13)
        self.cc_LineEdit.setObjectName(u"cc_LineEdit")
        self.cc_LineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.cc_LineEdit, 0, 7, 1, 1)

        self.label_43 = QLabel(self.groupBox_13)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font2)

        self.gridLayout_9.addWidget(self.label_43, 0, 8, 1, 1)

        self.label_46 = QLabel(self.groupBox_13)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font2)

        self.gridLayout_9.addWidget(self.label_46, 0, 6, 1, 1)

        self.label = QLabel(self.groupBox_13)
        self.label.setObjectName(u"label")
        self.label.setFont(font2)

        self.gridLayout_9.addWidget(self.label, 0, 0, 1, 1)

        self.d50_LineEdit = QLineEdit(self.groupBox_13)
        self.d50_LineEdit.setObjectName(u"d50_LineEdit")
        self.d50_LineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.d50_LineEdit, 0, 3, 1, 1)

        self.label_44 = QLabel(self.groupBox_13)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setFont(font2)

        self.gridLayout_9.addWidget(self.label_44, 0, 2, 1, 1)

        self.ci_LineEdit = QLineEdit(self.groupBox_13)
        self.ci_LineEdit.setObjectName(u"ci_LineEdit")
        self.ci_LineEdit.setReadOnly(True)

        self.gridLayout_9.addWidget(self.ci_LineEdit, 0, 9, 1, 1)

        self.gridLayout_9.setColumnStretch(0, 1)
        self.gridLayout_9.setColumnStretch(1, 1)
        self.gridLayout_9.setColumnStretch(2, 1)
        self.gridLayout_9.setColumnStretch(3, 1)
        self.gridLayout_9.setColumnStretch(4, 1)
        self.gridLayout_9.setColumnStretch(5, 1)
        self.gridLayout_9.setColumnStretch(6, 1)
        self.gridLayout_9.setColumnStretch(7, 1)
        self.gridLayout_9.setColumnStretch(8, 1)
        self.gridLayout_9.setColumnStretch(9, 1)

        self.verticalLayout.addWidget(self.groupBox_13)

        self.groupBox = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox.setObjectName(u"groupBox")
        self.groupBox.setFont(font)
        self.verticalLayout_2 = QVBoxLayout(self.groupBox)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.verticalLayout_2.setContentsMargins(0, 0, 0, 0)
        self.paramDistribution_MatplotlibWidget = QMatplotlibWidget(self.groupBox)
        self.paramDistribution_MatplotlibWidget.setObjectName(u"paramDistribution_MatplotlibWidget")

        self.verticalLayout_2.addWidget(self.paramDistribution_MatplotlibWidget)


        self.verticalLayout.addWidget(self.groupBox)

        self.groupBox_2 = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox_2.setObjectName(u"groupBox_2")
        self.groupBox_2.setFont(font)
        self.verticalLayout_7 = QVBoxLayout(self.groupBox_2)
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")
        self.verticalLayout_7.setContentsMargins(0, 0, 0, 0)
        self.grading_MatplotlibWidget = QMatplotlibWidget(self.groupBox_2)
        self.grading_MatplotlibWidget.setObjectName(u"grading_MatplotlibWidget")

        self.verticalLayout_7.addWidget(self.grading_MatplotlibWidget)


        self.verticalLayout.addWidget(self.groupBox_2)

        self.verticalLayout.setStretch(3, 8)
        self.verticalLayout.setStretch(4, 6)

        self.horizontalLayout.addLayout(self.verticalLayout)

        self.groupBox_12 = QGroupBox(MuckAnalysis_SubWidget)
        self.groupBox_12.setObjectName(u"groupBox_12")
        self.groupBox_12.setFont(font)
        self.gridLayout_8 = QGridLayout(self.groupBox_12)
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.gridLayout_8.setContentsMargins(0, 0, 0, 0)
        self.muckImage_Label = QLabel(self.groupBox_12)
        self.muckImage_Label.setObjectName(u"muckImage_Label")

        self.gridLayout_8.addWidget(self.muckImage_Label, 0, 0, 1, 1)


        self.horizontalLayout.addWidget(self.groupBox_12)

        self.horizontalLayout.setStretch(0, 4)
        self.horizontalLayout.setStretch(1, 6)

        self.retranslateUi(MuckAnalysis_SubWidget)

        QMetaObject.connectSlotsByName(MuckAnalysis_SubWidget)
    # setupUi

    def retranslateUi(self, MuckAnalysis_SubWidget):
        MuckAnalysis_SubWidget.setWindowTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u5ca9\u6e23\u56fe\u50cf\u5206\u6790", None))
        self.groupBox_10.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u91c7\u6837\u65f6\u95f4\u9009\u62e9", None))
        self.label_26.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u91c7\u6837\u65f6\u95f4", None))
        self.label_25.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u65e5\u671f", None))
        self.time_ComboBox.setItemText(0, QCoreApplication.translate("MuckAnalysis_SubWidget", u"00:02:00", None))

        self.groupBox_11.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u5b9e\u65f6\u6398\u8fdb\u53c2\u6570", None))
        self.label_41.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u63a8\u8fdb\u901f\u5ea6<br/>(mm/min)</p></body></html>", None))
        self.t_LineEdit.setText("")
        self.label_38.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u8d2f\u5165\u5ea6<br/>(mm/r)</p></body></html>", None))
        self.f_LineEdit.setText("")
        self.vr_LineEdit.setText("")
        self.label_37.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u603b\u63a8\u529b<br>(MN)</p></body></html>", None))
        self.label_40.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u5200\u76d8\u8f6c\u901f<br>(r/min)</p></body></html>", None))
        self.label_39.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u5200\u76d8\u626d\u77e9<br>(MN\u00b7m)</p></body></html>", None))
        self.pr_LineEdit.setText("")
        self.vp_LineEdit.setText("")
        self.groupBox_13.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u7ea7\u914d\u7279\u5f81", None))
        self.vol_LineEdit.setText("")
        self.label_45.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Cu</span></p></body></html>", None))
        self.cu_LineEdit.setText("")
        self.cc_LineEdit.setText("")
        self.label_43.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">CI</span></p></body></html>", None))
        self.label_46.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">Cc</span></p></body></html>", None))
        self.label.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\">\u603b\u4f53\u79ef<br>(m<span style=\" vertical-align:super;\">3</span>)</p></body></html>", None))
        self.d50_LineEdit.setText("")
        self.label_44.setText(QCoreApplication.translate("MuckAnalysis_SubWidget", u"<html><head/><body><p align=\"center\"><span style=\" font-style:italic;\">d</span><span style=\" vertical-align:sub;\">50</span>(mm)</p></body></html>", None))
        self.ci_LineEdit.setText("")
        self.groupBox.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u5ca9\u6e23\u5f62\u6001", None))
        self.groupBox_2.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u7ea7\u914d\u66f2\u7ebf", None))
        self.groupBox_12.setTitle(QCoreApplication.translate("MuckAnalysis_SubWidget", u"\u5ca9\u6e23\u56fe\u50cf", None))
        self.muckImage_Label.setText("")
    # retranslateUi

