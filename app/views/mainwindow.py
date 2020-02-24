from .ui.uiobjects import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow, QSizePolicy

from .teamconfigview import TeamConfigView
from .logfileprocessingview import LogFileProcessingView
from .testGraphView import ListGraphView

# TODO: Make application responsive, where all UI elements positions
# adapt to the size of the window

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #   self.setFixedSize(self.ui.gridLayout.sizeHint())
        # sizePolicy = QSizePolicy(QSizePolicy.Expanding, QSizePolicy.Expanding)
        # sizePolicy.setHorizontalStretch(0)
        # sizePolicy.setVerticalStretch(0)
        # sizePolicy.setHeightForWidth(self.sizePolicy().hasHeightForWidth())
        # self.setSizePolicy(sizePolicy)
        self.ui.gridLayout
        self.keyPressEvent = self.keyPress
        self.ui.nextView.clicked.connect(self.nextview)
        self.ui.newProjectAction.triggered.connect(self.teamconfig)

    def keyPress(self, e): 
        from PyQt5 import QtCore
        if e.key() == QtCore.Qt.Key_Escape:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.nextView.clicked.connect(self.nextview)
            self.ui.newProjectAction.triggered.connect(self.teamconfig)

    def teamconfig(self):
        TeamConfigView(self)

    def new_project(self): 
        self.resize(1150,950)
        process = LogFileProcessingView(self)
        self.setCentralWidget(process)
        process.startProcess()
    
    def actionreport_view(self):
        pass

    def nextview(self):
        graph = ListGraphView(self)
        # self.takeCentralWidget()
        # self.hide()
        # graph.show()
        self.setCentralWidget(graph)