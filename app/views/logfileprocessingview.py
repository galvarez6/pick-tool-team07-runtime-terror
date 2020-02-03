from .ui.uiobjects import Ui_LogFileProcessing

from PyQt5.QtWidgets import QWidget

class LogFileProcessingView(QWidget):
    def __init__(self, parent):
        super(LogFileProcessingView, self).__init__(parent) 
        print("hello")
        self.parent = parent
        self.ui = Ui_LogFileProcessing()
        self.ui.setupUi(self)
        self.parent.setCentralWidget(self)
        # self.parent.exec()