from PyQt5.QtWidgets import QMainWindow, QAction

from .projectconfigview import ProjectConfigView
from .analysisview import AnalysisView

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self): 
        self.showMaximized()
        self.setupMenuBar()

        self.analysisView = AnalysisView()
        self.setCentralWidget(self.analysisView)

    def setupMenuBar(self): 
        # Menu Bar
        self.newProject = QAction("New Project", self)
        self.newProject.triggered.connect(self.new_project)

        self.menubar = self.menuBar()
        self.filemenu = self.menubar.addMenu("File")
        self.filemenu.addAction(self.newProject)

    def keyPress(self, e): 
        from PyQt5 import QtCore
        if e.key() == QtCore.Qt.Key_Escape:
            self.ui = Ui_MainWindow()
            self.ui.setupUi(self)
            self.ui.nextView.clicked.connect(self.nextview)
            self.ui.newProjectAction.triggered.connect(self.teamconfig)

    def teamconfig(self):
        ProjectConfigView(self)

    def new_project(self): 
        print("New Project")
        ProjectConfigView(self)
        # self.resize(1150,950)
        # process = LogFileProcessingView(self)
        # self.setCentralWidget(process)
        # process.startProcess()
    
    def actionreport_view(self):
        pass

    def nextview(self):
        self.resize(1500, 1150)
        graph = ListGraphView(self)
        # self.takeCentralWidget()
        # self.hide()
        # graph.show()
        self.setCentralWidget(graph)