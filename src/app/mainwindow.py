from PyQt5.QtWidgets import QMainWindow, QAction

from app.views.analysisview import AnalysisView
from app.views.processingview import ProcessingView
from app.dialogs.projectconfigdialog import ProjectConfigDialog

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self): 
        self.setMinimumSize(500,500)
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
        pass

    def new_project(self):
        ProjectConfigDialog(self)