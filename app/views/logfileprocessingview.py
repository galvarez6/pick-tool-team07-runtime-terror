import os

from PyQt5 import QtWidgets

from .ui.uiobjects import Ui_LogFileProcessing

from PyQt5.QtWidgets import QWidget, QTableWidgetItem


class LogFileProcessingView(QWidget):
    def __init__(self, parent):
        super(LogFileProcessingView, self).__init__(parent) 
        self.parent = parent
        self.ui = Ui_LogFileProcessing()
        self.ui.setupUi(self)
        self.parent.setCentralWidget(self)
        #self.exec()
        self.startProcess()

    def startProcess(self):
        row = 0
        #root_dir will come from event config right?
        for dirName, subdirList, fileList in os.walk(root_dir, topdown=False):
            print('Found directory: %s' % dirName)
            # source = QTableWidgetItem(dirName)
            # self.ui.logfiletable.setItem(row, 1, source)
            for fname in fileList:
                print('\t%s' % fname)
                info = QTableWidgetItem(fname)
                checkBox = QtWidgets.QCheckBox()
                source = QTableWidgetItem(dirName)
                self.ui.logfiletable.setItem(row, 1, source)
                self.ui.logfiletable.setItem(row, 0, info)
                self.ui.logfiletable.setCellWidget(row, 5, checkBox)
                row += 1

