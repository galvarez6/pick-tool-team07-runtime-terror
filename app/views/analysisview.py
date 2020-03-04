from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout, QVBoxLayout, QTableView,\
                            QTableWidget, QTabWidget, QListWidget, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QAction

class AnalysisView(QWidget): 
    def __init__(self, parent=None): 
        super(QWidget, self).__init__(parent)
        self.initUI()

    def initUI(self): 
        self.setupMainLayout()
        self.setLayout(self.mainLayout)

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