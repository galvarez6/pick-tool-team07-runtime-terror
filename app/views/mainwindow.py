from .ui.uiobjects import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow

from .teamconfigview import TeamConfigView
from .logfileprocessingview import LogFileProcessingView

# TODO: Make application responsive, where all UI elements positions
# adapt to the size of the window

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        # self.showMaximized()
        self.ui.newProjectAction.triggered.connect(self.teamconfig)

    def teamconfig(self): 
        TeamConfigView(self)

    def new_project(self): 
        self.resize(1150,950)
        LogFileProcessingView(self)
    
    def actionreport_view(self):
        pass