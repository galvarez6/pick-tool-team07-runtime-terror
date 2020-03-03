from .ui.uiobjects import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow,QWidget,QFrame, QGridLayout,QHBoxLayout,QVBoxLayout,QTableView,QTableWidget,QTabWidget,QListWidget,QLineEdit,QComboBox,QSpacerItem,QSizePolicy,QAction

from .projectconfigview import ProjectConfigView
from .logfileprocessingview import LogFileProcessingView
from .testGraphView import ListGraphView

# TODO: Make application responsive, where all UI elements positions
# adapt to the size of the window

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        self.initUI()

    def initUI(self): 
        self.showMaximized()
        self.setupMenuBar()
        self.setupMainLayout()

        self.widget = QWidget()
        self.widget.setLayout(self.mainLayout)
        self.setCentralWidget(self.widget)

    def setupMenuBar(self): 
        # Menu Bar
        self.newProject = QAction("New Project", self)
        self.newProject.triggered.connect(self.new_project)

        self.menubar = self.menuBar()
        self.filemenu = self.menubar.addMenu("File")
        self.filemenu.addAction(self.newProject)

    def setupMainLayout(self): 
        #Log Entries table
        self.logEntriesTbl = QTableView()
        self.setupVectorTab()
        self.tabWidget = QTabWidget()
        self.tabWidget.addTab(self.logEntriesTbl, "Log Entries")
        self.tabWidget.addTab(self.vectorFrame, "Vector View")

        # Defined Vectors list
        self.vectorWidget = QListWidget()

        self.workspace = QHBoxLayout()
        self.workspace.addWidget(self.vectorWidget, 10)
        self.workspace.addWidget(self.tabWidget,90)

        # Filtering and search
        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.search = QLineEdit()
        self.filterBox = QComboBox()

        # Container for tab/table controls 
        self.controls = QHBoxLayout()
        self.controls.addItem(hSpacer)
        self.controls.addWidget(self.search)
        self.controls.addWidget(self.filterBox)

        # Container for all workspace
        self.mainLayout = QVBoxLayout()
        self.mainLayout.addLayout(self.controls)
        self.mainLayout.addLayout(self.workspace)

    def setupVectorTab(self): 
        self.graph = QVBoxLayout()
        self.nodes = QTableWidget()

        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        self.orientationCb = QComboBox()
        self.unitsCb = QComboBox()
        self.interval = QLineEdit()

        # Graph controls such as orientation, interval units, interval
        self.graphContols = QHBoxLayout()
        self.graphContols.addItem(hSpacer)
        self.graphContols.addWidget(self.orientationCb)
        self.graphContols.addWidget(self.unitsCb)
        self.graphContols.addWidget(self.interval)

        self.vectorViews = QHBoxLayout()
        self.vectorViews.addLayout(self.graph)
        self.vectorViews.addWidget(self.nodes)

        self.container = QVBoxLayout()
        self.container.addLayout(self.graphContols)
        self.container.addLayout(self.vectorViews)

        self.vectorFrame = QFrame()
        self.vectorFrame.setLayout(self.container)

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