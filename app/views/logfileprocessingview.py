import os
import sys
sys.path.append("..")

from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_LogFileProcessing

from PyQt5 import QtWidgets
from PyQt5.QtCore import QSettings
from PyQt5.QtWidgets import QWidget, QTableWidgetItem, QDialog

class LogFileProcessingView(QWidget):
    def __init__(self, parent):
        super(LogFileProcessingView, self).__init__(parent) 
        self.eventConfig = EventConfigManager.get_instance().getEventConfig()
        self.parent = parent
        self.ui = Ui_LogFileProcessing()
        self.ui.setupUi(self)
        self.ui.logfiletable.setColumnCount(6)
        self.ui.logfiletable.setRowCount(50)
        # self.parent.setCentralWidget(self)
        # self.startProcess()
        self.ui.pushButton.clicked.connect(self.cancelClicked)

    def startProcess(self):
        row = 0
        #root_dir will come from event config right?
        root_dir = self.eventConfig.rootDir
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
        

        
        

        
