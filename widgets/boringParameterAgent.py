import PySide2.QtCore as QtC
import pandas as pd
import numpy as np
import random
from pathlib import Path
import warnings
import datetime
# from .daemonWorker import DaemonWorker

class DummyBoringParameterAgent(QtC.QObject):
    sendSampleToWorker = QtC.Signal(tuple, tuple, tuple)
    startSendBoringParameter = QtC.Signal(datetime.datetime)
    stopSendBoringParameter = QtC.Signal(datetime.datetime)


    def loadBoringParameterInfo(self):
        self.sample_queue = [[], [], [], []]
        self.prefetch_count = self.config.BORING_PARAMETER.PREFETCH_COUNT
        self.data_fld = Path.cwd() / self.config.BORING_PARAMETER.DATA_FLD
        data_info_path = Path.cwd() / self.config.BORING_PARAMETER.DATA_INFO_PATH
        self.data_info = pd.read_excel(data_info_path)
        self.data_info['opened'] = 0
        self.load_to_buffer()

    @property
    def readyToSend(self):
        return list(len(self.sample_queue[i]) > 0 for i in [0, 1, 2, 3])

    def process_sample(self, path):
        orig_df = pd.read_excel(path)
        stable_start = int(orig_df['稳定段起点'].loc[0]) + 5
        stable_end = int(orig_df['稳定段终点'].loc[0]) - 5
        start_time = orig_df['时间'].loc[0]

        with warnings.catch_warnings():
            warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)
            df = pd.DataFrame(columns=['time', 'pr', 'f', 'vr', 't', 'vp'])
            df['time'] = orig_df.apply(lambda row: (row['时间'] - start_time).seconds, axis=1)
            df[['pr', 'f', 'vr', 't', 'vp']] = orig_df[['推进速度', '推力', '刀盘转速', '刀盘扭矩', '贯入度']]
            df['f'] = df['f'] / 1000
            df['t'] = df['t'] / 1000

            x_pre = df['time'].loc[:stable_start].to_numpy()
            y_pre = df[['pr', 'f', 'vr', 't', 'vp']].loc[:stable_start].to_numpy()
            x_stable = df['time'].loc[stable_start: stable_end].to_numpy()
            y_stable = df[['pr', 'f', 'vr', 't', 'vp']].loc[stable_start: stable_end].to_numpy()
            x_end = df['time'].loc[stable_end:].to_numpy()
            y_end = df[['pr', 'f', 'vr', 't', 'vp']].loc[stable_end:].to_numpy()

        return (x_pre, y_pre), (x_stable, y_stable), (x_end, y_end)

    def load_to_buffer(self):
        for i in [0, 1, 2, 3]:
            while len(self.sample_queue[i]) < self.prefetch_count:
                available_index = (
                    self.data_info[
                        self.data_info['rock_grade'] == i
                        ].loc[
                        self.data_info['opened'] == 0
                        ]
                ).index
                if len(available_index) == 0:
                    break
                idx = random.choice(available_index)
                self.sample_queue[i].append(
                    self.process_sample(self.data_fld / f"{self.data_info['name'].loc[idx]}.xlsx")
                )
                with warnings.catch_warnings():
                    warnings.filterwarnings('ignore', category=pd.errors.SettingWithCopyWarning)
                    self.data_info['opened'].loc[idx] = 1

    @QtC.Slot(datetime.datetime, float)
    def onStartBoringCycleSignalReceived(self, beginTime, beginMileage):
        if self.readyToSend[self.current_grade]:
            sample = self.sample_queue[self.current_grade].pop(0)
            self.sendSampleToWorker.emit(*sample)
            self.startSendBoringParameter.emit(datetime.datetime.now())
            self.load_to_buffer()

    @QtC.Slot(datetime.datetime, float)
    def onStopBoringCycleSignalReceived(self, endTime, endMileage):
        pass