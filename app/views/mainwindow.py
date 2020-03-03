from .ui.uiobjects import Ui_MainWindow

from PyQt5.QtWidgets import QMainWindow,QWidget,QGridLayout,QHBoxLayout,QVBoxLayout,QTableView,QTabWidget,QListWidget,QLineEdit,QComboBox,QSpacerItem,QSizePolicy,QAction

from .teamconfigview import TeamConfigView
from .logfileprocessingview import LogFileProcessingView
from .testGraphView import ListGraphView

# TODO: Make application responsive, where all UI elements positions
# adapt to the size of the window

class MainWindow(QMainWindow): 
    def __init__(self):
        super(MainWindow, self).__init__()
        # self.ui = Ui_MainWindow()
        # self.ui.setupUi(self)
        # self.keyPressEvent = self.keyPress
        # self.ui.nextView.clicked.connect(self.nextview)
        # self.ui.newProjectAction.triggered.connect(self.teamconfig)
        self.initUI()

    def initUI(self): 
        self.showMaximized()

        # Menu Bar
        newProject = QAction("New Project", self)
        newProject.triggered.connect(self.new_project)

        menubar = self.menuBar()
        filemenu = menubar.addMenu("File")
        filemenu.addAction(newProject)

        #Log Entries table
        logEntriesTbl = QTableView()
        # TODO: Add vector view to tab widget
        tabWidget = QTabWidget()
        tabWidget.addTab(logEntriesTbl, "Log Entries")

        # Defined Vectors list
        vectorWidget = QListWidget()

        workspace = QHBoxLayout()
        workspace.addWidget(vectorWidget, 15)
        workspace.addWidget(tabWidget,85)

        # Filtering and search
        hSpacer = QSpacerItem(0, 0, QSizePolicy.Expanding, QSizePolicy.Fixed)
        search = QLineEdit()
        filterBox = QComboBox()

        # Container for tab/table controls 
        controls = QHBoxLayout()
        controls.addItem(hSpacer)
        controls.addWidget(search)
        controls.addWidget(filterBox)


        mainLayout = QVBoxLayout()
        mainLayout.addLayout(controls)
        mainLayout.addLayout(workspace)

        widget = QWidget()
        widget.setLayout(mainLayout)
        self.setCentralWidget(widget)

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
        print("New Project")
        # self.resize(1150,950)
        # process = LogFileProcessingView(self)
        # self.setCentralWidget(process)
        # process.startProcess()
    
    def actionreport_view(self):
        pass

    def nextview(self):
        graph = ListGraphView(self)
        # self.takeCentralWidget()
        # self.hide()
        # graph.show()
        self.setCentralWidget(graph)