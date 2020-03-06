from PyQt5.QtWidgets import QMainWindow, QAction

from app.views.analysisview import AnalysisView
from app.views.processingview import ProcessingView
from app.dialogs.projectconfigdialog import ProjectConfigDialog

from enum import Enum

class VIEW(Enum): 
    ANALYSIS = 0x1
    PROCESSING = 0x2

# TODO: Add save and restoring abilities to the application
class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self): 
        self.setMinimumSize(500,500)
        self.showMaximized()
        self.setupMenuBar()

        # TODO: Create a stack widget and add these views to the stack widget,
        # so that we can navigate between both of these views. 
        # Also, I think QStackWidgets saves the state of each of the widgets
        # that it holds, so that works on our favor. 
        self.analysisView = AnalysisView(self)
        self.processingView = ProcessingView(self)
        self.view = VIEW.ANALYSIS
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
        # TODO: Add better implemenation for this dialog, aka
        # make an instance of the dialog and execute it from here and 
        # not from the ProjectConfigDialog itself.
        ProjectConfigDialog(self)

    # TODO: Update this implementation to work with StackWidget
    def updateView(self): 
        # This is a simple hack that I have to change the main window views for now
        # once the StackWidget has been added this code will change. 
        if self.view == VIEW.ANALYSIS: 
            self.view = VIEW.PROCESSING
            self.setCentralWidget(self.processingView)
        elif self.view == VIEW.PROCESSING: 
            self.view = VIEW.ANALYSIS
            self.analysisView.updateVectorList()
            self.setCentralWidget(self.analysisView)
