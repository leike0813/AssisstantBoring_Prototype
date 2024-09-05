import datetime
import math
import random
import numpy as np
import pandas as pd
import scipy.stats as stats
from collections import Counter
from pathlib import Path
import PySide2.QtCore as QtC, PySide2.QtWidgets as QtW
from .boringParameterAgent import DummyBoringParameterAgent
from workers import DaemonWorker, NNWorker, PostProcWorker, ImageMonitorWorker
from workers.boringParameterWorker import DummyBoringParameterWorker


__all__ = ['DaemonWidget']


OTHER_DICTS = [
    {
        'bolt_spec': '无',
        'bolt_length': '',
        'bolt_cir_spacing': '',
        'bolt_longi_spacing': '',
        'bolt_angle': '',
        'arch_spec': '无',
        'arch_spacing': '',
        'net_spec': '无',
        'net_angle': '',
        'shotcrete_strength': '无',
        'shotcrete_thickness': '',
        'shotcrete_in_time': '',
        'liner_strength': 'C35',
        'liner_thickness': '30',
        'others': '',
        'jamming_risk': '低',
        'jamming_measure': '适度控制推力，关注岩爆风险，平稳连续掘进。'
    },
    {
        'bolt_spec': 'φ25',
        'bolt_length': '2.0~2.5 m',
        'bolt_cir_spacing': '随机',
        'bolt_longi_spacing': '随机',
        'bolt_angle': '随机',
        'arch_spec': '无',
        'arch_spacing': '',
        'net_spec': 'φ8×φ8@200',
        'net_angle': '180°',
        'shotcrete_strength': 'C30',
        'shotcrete_thickness': '15 cm',
        'shotcrete_in_time': '否',
        'liner_strength': 'C35',
        'liner_thickness': '30 cm',
        'others': '',
        'jamming_risk': '低',
        'jamming_measure': '维持正常推力及转速，平稳连续掘进。'
    },
    {
        'bolt_spec': 'φ25',
        'bolt_length': '2.5~3.0 m',
        'bolt_cir_spacing': '1.2~1.5 m',
        'bolt_longi_spacing': '1.5~2.0 m',
        'bolt_angle': '180°',
        'arch_spec': 'HW100',
        'arch_spacing': '1.5~2.0 m',
        'net_spec': 'φ8×φ8@200',
        'net_angle': '180°',
        'shotcrete_strength': 'C30',
        'shotcrete_thickness': '15 cm',
        'shotcrete_in_time': '否',
        'liner_strength': 'C35',
        'liner_thickness': '30 cm',
        'others': '',
        'jamming_risk': '低',
        'jamming_measure': '维持正常推力及转速，平稳连续掘进。'
    },
    {
        'bolt_spec': 'φ25',
        'bolt_length': '3.0~3.5 m',
        'bolt_cir_spacing': '1.2~1.5 m',
        'bolt_longi_spacing': '0.8~1.2 m',
        'bolt_angle': '180°',
        'arch_spec': 'HW150',
        'arch_spacing': '0.8~1.2 m',
        'net_spec': 'φ8×φ8@200',
        'net_angle': '180°',
        'shotcrete_strength': 'C30',
        'shotcrete_thickness': '20 cm',
        'shotcrete_in_time': '根据情况选择',
        'liner_strength': 'C35',
        'liner_thickness': '30 cm',
        'others': '',
        'jamming_risk': '中',
        'jamming_measure': '适当控制推力及转速，避免过度扰动围岩，平稳连续掘进。'
    },
    {
        'bolt_spec': 'φ25',
        'bolt_length': '无',
        'bolt_cir_spacing': '',
        'bolt_longi_spacing': '',
        'bolt_angle': '',
        'arch_spec': 'HW150',
        'arch_spacing': '0.6~0.8 m',
        'net_spec': 'φ8×φ8@200',
        'net_angle': '180°',
        'shotcrete_strength': 'C30',
        'shotcrete_thickness': '20 cm',
        'shotcrete_in_time': '是',
        'liner_strength': 'C35',
        'liner_thickness': '40 cm',
        'others': '必要时可采用管棚辅助稳定地层。',
        'jamming_risk': '高',
        'jamming_measure': '采用较低的推力及转速，监控隧洞变形，稳步掘进通过。'
    },
]


def sample_with_quantile(dist, quantile_range=[0.05, 0.95], max_try=100):
    sample_range = [dist.ppf(i) for i in quantile_range]
    i = 0
    while True:
        sample = dist.rvs()
        i += 1
        if (sample >= sample_range[0] and sample <= sample_range[1]) or i >= max_try:
            break
    return sample


class DaemonWidget(QtW.QWidget, DummyBoringParameterAgent):
    startBoringCycle = QtC.Signal(datetime.datetime, float)
    stopBoringCycle = QtC.Signal(datetime.datetime, float)
    plotRockInformation = QtC.Signal(float, list)
    showMileageInformation = QtC.Signal(str, str, float, float, int, int, float, float, dict)


    def __init__(self, mainWindow=None, parent=None):
        super(DaemonWidget, self).__init__(parent)
        self.mainWindow = mainWindow
        self.config = mainWindow.config

        self.ucs_Dists = [stats.genhyperbolic(*i) for i in self.config.GENERAL.UCS_DIST_PARAMS]
        self.kv_Dists = [stats.genhyperbolic(*i) for i in self.config.GENERAL.KV_DIST_PARAMS]
        self.f_Dists = [stats.genhyperbolic(*i) for i in self.config.GENERAL.F_DIST_PARAMS]
        self.vr_Dists = [stats.genhyperbolic(*i) for i in self.config.GENERAL.VR_DIST_PARAMS]
        self.cycleRockGrades = []
        self.current_mileage = self.config.GENERAL.CURRENT_MILEAGE
        self.current_grade = self.config.GENERAL.CURRENT_GRADE

        self.loadBoringParameterInfo()

        self.daemonWorker = DaemonWorker(self)
        self.daemonWorker.sendText2DaemonWidget.connect(self.addText)
        self.daemonWorker.sendText.connect(self.mainWindow.statusBarShowMessage)
        self.daemonThread = QtC.QThread()
        self.daemonWorker.moveToThread(self.daemonThread)
        self.daemonThread.start()

        self.nnWorker = NNWorker(self)
        self.nnWorker.sendText2DaemonWidget.connect(self.addText)
        self.nnWorker.sendText.connect(self.mainWindow.statusBarShowMessage)
        self.nnThread = QtC.QThread()
        self.nnWorker.moveToThread(self.nnThread)
        self.nnThread.start()

        self.postProcWorker = PostProcWorker(self)
        self.postProcWorker.sendText2DaemonWidget.connect(self.addText)
        self.postProcWorker.sendText.connect(self.mainWindow.statusBarShowMessage)
        self.postProcThread = QtC.QThread()
        self.postProcWorker.moveToThread(self.postProcThread)
        self.postProcThread.start()

        self.imageMonitorWorker = ImageMonitorWorker(self)
        self.imageMonitorWorker.sendText2DaemonWidget.connect(self.addText)
        self.imageMonitorWorker.sendText.connect(self.mainWindow.statusBarShowMessage)
        self.imageMonitorThread = QtC.QThread()
        self.imageMonitorWorker.moveToThread(self.imageMonitorThread)

        self.imageMonitorWorker.findNewImage.connect(self.onFindNewImage)
        self.imageMonitorWorker.idleThreshExceeded.connect(self.onIdleThreshExceeded)
        self.imageMonitorWorker.sendImagePath.connect(self.nnWorker.enqueueImage)

        self.imageMonitorThread.started.connect(self.imageMonitorWorker.run)
        self.imageMonitorThread.start()

        self.boringParameterWorker = DummyBoringParameterWorker(self)
        self.boringParameterWorker.sendText2DaemonWidget.connect(self.addText)
        self.boringParameterWorker.sendText.connect(self.mainWindow.statusBarShowMessage)
        self.boringParameterThread = QtC.QThread()
        self.boringParameterWorker.moveToThread(self.boringParameterThread)
        self.boringParameterThread.start()

        self.plotRockInformation.connect(self.mainWindow.monitor_SubWidget.plotRockInformation)
        self.showMileageInformation.connect(self.mainWindow.monitor_SubWidget.showMileageInformation)
        self.nnWorker.inferenceComplete.connect(self.postProcWorker.enqueueImage)
        self.postProcWorker.plotMuckImage.connect(self.mainWindow.monitor_SubWidget.plotMuckImage)
        self.postProcWorker.plotMuckParameter.connect(self.mainWindow.monitor_SubWidget.plotMuckParameter)
        self.postProcWorker.sendRockGrade.connect(self.onRockGradeReceived)

        self.startBoringCycle.connect(self.onStartBoringCycleSignalReceived)
        self.startBoringCycle.connect(self.mainWindow.monitor_SubWidget.onStartBoringCycleSignalReceived)
        self.stopBoringCycle.connect(self.onStopBoringCycleSignalReceived)
        self.stopBoringCycle.connect(self.mainWindow.monitor_SubWidget.onStopBoringCycleSignalReceived)

        self.sendSampleToWorker.connect(self.boringParameterWorker.onSampleReceived)
        self.startSendBoringParameter.connect(self.boringParameterWorker.onStartSendBoringParameterSignalReceived)
        self.stopSendBoringParameter.connect(self.boringParameterWorker.onStopSendBoringParameterSignalReceived)
        self.boringParameterWorker.sendBoringParameter.connect(self.mainWindow.monitor_SubWidget.plotBoringParameter)
        self.boringParameterWorker.boringParameterSendingComplete.connect(self.onBoringParameterSendingComplete)

        self.workers = [
            self.daemonWorker,
            self.nnWorker,
            self.postProcWorker,
            self.imageMonitorWorker,
            self.boringParameterWorker,
        ]
        self.workerThreads = [
            self.daemonThread,
            self.nnThread,
            self.postProcThread,
            self.imageMonitorThread,
            self.boringParameterThread,
        ]

        self.setupUi()

    def setupUi(self):
        self.setObjectName(u"DaemonWidget")
        self.resize(800, 400)
        self.verticalLayout = QtW.QVBoxLayout(self)
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.textBrowser = QtW.QTextBrowser(self)
        self.textBrowser.setObjectName(u"textBrowser")
        self.verticalLayout.addWidget(self.textBrowser)

        self.setWindowTitle(QtC.QCoreApplication.translate("DaemonWidget", u"\u540e\u53f0\u76d1\u63a7\u5668", None))

        QtC.QMetaObject.connectSlotsByName(self)

    def closeEvent(self, event):
        for thread in self.workerThreads:
            if thread.isRunning():
                thread.quit()
                thread.wait()

        super().closeEvent(event)

    @QtC.Slot(str)
    def addText(self, text):
        self.textBrowser.setText(self.textBrowser.toPlainText() + '\n' + text)
        self.textBrowser.verticalScrollBar().setValue(self.textBrowser.verticalScrollBar().maximum())

    @QtC.Slot(datetime.datetime, float)
    def onStartBoringCycleSignalReceived(self, beginTime, beginMileage):
        super(DaemonWidget, self).onStartBoringCycleSignalReceived(beginTime, beginMileage)
        self.postProcWorker.cur_cycle_begin = beginTime
        self.cycleRockGrades = []

    @QtC.Slot(datetime.datetime, float)
    def onStopBoringCycleSignalReceived(self, endTime, endMileage):
        super(DaemonWidget, self).onStopBoringCycleSignalReceived(endTime, endMileage)
        if len(self.cycleRockGrades) > 0:
            counter = Counter(self.cycleRockGrades)
            current_grade = counter.most_common(1)[0][0]
            self.inferAndShowInformations(endMileage, current_grade)

    @QtC.Slot(int)
    def onRockGradeReceived(self, grade):
        self.cycleRockGrades.append(grade)

    @QtC.Slot(datetime.datetime)
    def onFindNewImage(self, _time):
        self.startBoringCycle.emit(_time, self.current_mileage)

    @QtC.Slot(datetime.datetime)
    def onIdleThreshExceeded(self, _time):
        # self.stopBoringCycle.emit(_time, self.current_mileage)
        self.stopSendBoringParameter.emit(_time)

    @QtC.Slot(datetime.datetime, float)
    def onBoringParameterSendingComplete(self, _time, mileage_increment):
        self.current_mileage += mileage_increment
        self.stopBoringCycle.emit(_time, self.current_mileage)

    @QtC.Slot(float, int)
    def inferAndShowInformations(self, mileage, grade):
        mileage_head, mileage_tail, mileage_text = self.mileageParser(mileage)
        current_grade_text = self.config.GENERAL.ROCK_GRADES[grade]
        # current_ucs = sample_with_quantile(self.ucs_Dists[grade])
        # current_kv = sample_with_quantile(self.kv_Dists[grade])
        # suggest_f_eco = int(sample_with_quantile(self.f_Dists[grade], [0.1, 0.5]))
        # suggest_f_perf = int(sample_with_quantile(self.f_Dists[grade], [0.5, 0.9]))
        # suggest_vr_eco = sample_with_quantile(self.vr_Dists[grade], [0.1, 0.5])
        # suggest_vr_perf = sample_with_quantile(self.vr_Dists[grade], [0.5, 0.9])
        current_ucs = self.ucs_Dists[grade].rvs()
        current_kv = self.kv_Dists[grade].rvs()
        suggest_f = self.f_Dists[grade].mean()
        suggest_f_eco = int(suggest_f * (1 - 0.2 * random.random()))
        suggest_f_perf = int(suggest_f * (1 + 0.2 * random.random()))
        suggest_vr = self.vr_Dists[grade].mean()
        suggest_vr_eco = round(suggest_vr * (1 - 0.3 * random.random()), 1)
        suggest_vr_perf = round(suggest_vr * (1 + 0.3 * random.random()), 1)
        other_dict = OTHER_DICTS[grade]
        self.plotRockInformation.emit(mileage, [grade, current_ucs, current_kv])
        self.showMileageInformation.emit(mileage_text, current_grade_text, current_ucs, current_kv,
                                         suggest_f_eco, suggest_f_perf, suggest_vr_eco, suggest_vr_perf,
                                         other_dict)

    def mileageParser(self, mileage):
        mileage_head = self.config.GENERAL.MILEAGE_BASE + int(mileage // 1000)
        mileage_tail = mileage % 1000
        mileage_decimal, mileage_integer = math.modf(mileage_tail)
        mileage_integer = int(mileage_integer)
        mileage_string = f"{self.config.GENERAL.MILEAGE_MARK}{mileage_head}+{mileage_integer:03}.{round(mileage_decimal * 100)}"
        return mileage_head, mileage_tail, mileage_string
