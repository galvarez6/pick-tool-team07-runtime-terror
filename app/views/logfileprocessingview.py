import os

import sys

from PyQt5 import QtWidgets

from .ui.uiobjects import Ui_LogFileProcessing

from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog

#import mainwindow

root_dir = '/Users/joseg/Desktop/Spring2020/SW2/pick-tool-team07-runtime-terror/test/RootDir'

class LogFileProcessingView(QWidget):
    def __init__(self, parent):
        super(LogFileProcessingView, self).__init__(parent) 
        self.parent = parent
        self.ui = Ui_LogFileProcessing()
        self.ui.setupUi(self)
        self.ui.logfiletable.setColumnCount(6)
        self.ui.logfiletable.setRowCount(50)
        self.parent.setCentralWidget(self)
        self.startProcess()
        self.ui.pushButton.clicked.connect(self.cancelClicked)

    def startProcess(self):
        row = 0
        #root_dir will come from event config right?
        for dirName, subdirList, fileList in os.walk(root_dir, topdown=False):
            print('Found directory: %s' % dirName)
            for fname in fileList:
                print('\t%s' % fname)
                info = QTableWidgetItem(fname)
                checkBox = QtWidgets.QCheckBox()
                source = QTableWidgetItem(dirName)
                self.ui.logfiletable.setItem(row, 1, source)
                self.ui.logfiletable.setItem(row, 0, info)
                self.ui.logfiletable.setCellWidget(row, 5, checkBox)
                row += 1

    def cancelClicked(self):
        print("hello")
        

        
        

        
