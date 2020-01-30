import os
ui_dir = os.path.dirname(os.path.abspath(__file__))

from PyQt5 import uic
from PyQt5.QtWidgets import *

from .leadview import LeadView

Ui_MainWindow, _ = uic.loadUiType(ui_dir+r'/ui/PICK_App.ui')

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.newproject_qaction.triggered.connect(self.lead_view)

    def lead_view(self): 
        lead_widget = LeadView(self)
    
    def actionreport_view(self):
        pass