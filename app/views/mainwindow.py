from .ui.uiobjects import Ui_MainWindow

from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow

from .leadview import LeadView

# TODO: Make application responsive, where all UI elements positions
# adapt to the size of the window

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()
        self.ui.newproject_qaction.triggered.connect(self.lead_view)

    def lead_view(self): 
        lead_widget = LeadView(self)
    
    def actionreport_view(self):
        pass