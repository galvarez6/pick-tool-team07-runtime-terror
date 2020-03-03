import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_TeamConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QListWidget, QStackedWidget, QTableView, QVBoxLayout, QHBoxLayout, QLabel, QLineEdit, QPushButton, QRadioButton, QLineEdit

from .eventconfigview import EventConfigView

class ProjectConfigView(QDialog): 
    def __init__(self, parent):
        super(ProjectConfigView, self).__init__(parent)
        self.initUI()

    def initUI(self): 

        self.teamConfig = QWidget()
        self.dirConfig = QWidget()
        self.eventConfig = QWidget()
        self.vectorConfig = QWidget()

        self.teamConfigSetup()
        self.dirConfigSetup()
        
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamConfig)
        self.stack.addWidget(self.dirConfig)


        self.viewList = QListWidget()
        self.viewList.insertItem(0, "Team Configuration")
        self.viewList.insertItem(1, "Directory Configuration")
        self.viewList.insertItem(2, "Event Configuration")
        self.viewList.insertItem(3, "Vector Configuration")
        self.viewList.currentRowChanged.connect(lambda i : self.stack.setCurrentIndex(i))

        viewContainer = QHBoxLayout(self)
        viewContainer.addWidget(self.viewList, 30)
        viewContainer.addWidget(self.stack, 60)

        self.setLayout(viewContainer)
        self.exec_()
    
    def teamConfigSetup(self): 
        viewLabel = QLabel()
        viewLabel.setText("Team Configuration")
        viewLabel.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

        self.leadRbtn = QRadioButton()
        self.leadRbtn.setText("Lead")

        self.leadIpLbl = QLabel()
        self.leadIpLbl.setText("Lead IP Address")
        self.leadIp = QLineEdit()
        
        self.ipContainer = QHBoxLayout()
        self.ipContainer.addWidget(self.leadIpLbl)
        self.ipContainer.addWidget(self.leadIp)

        self.connectionsLbl = QLabel()
        self.connectionsLbl.setText("Connections")

        self.connectionsView = QTableView()

        self.connectBtn = QPushButton()
        self.connectBtn.setText("Connect")
        self.connectBtn.clicked.connect(self.connect)


        teamViewContainer = QVBoxLayout()
        teamViewContainer.addWidget(viewLabel)
        teamViewContainer.addWidget(self.leadRbtn)
        teamViewContainer.addLayout(self.ipContainer)
        teamViewContainer.addWidget(self.connectionsLbl)
        teamViewContainer.addWidget(self.connectionsView)
        teamViewContainer.addWidget(self.connectBtn)

        self.teamConfig.setLayout(teamViewContainer)

    def dirConfigSetup(self): 
        viewLabel = QLabel()
        viewLabel.setText("Directory Configuration")
        viewLabel.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)
        viewLabelCon = QHBoxLayout()
        viewLabelCon.addWidget(viewLabel)

        # Root directory controls
        rootDirLbl = QLabel("Root Directory")
        self.rootDirPath = QLineEdit()
        self.rootDirBrowse = QPushButton()
        self.rootDirBrowse.setText("Browse")
        

        # Root Directory controls container
        rootDirContainer = QHBoxLayout()
        rootDirContainer.addWidget(rootDirLbl)
        rootDirContainer.addWidget(self.rootDirPath)
        rootDirContainer.addWidget(self.rootDirBrowse)

        # Red Folder controls
        redFolderLbl = QLabel("Red Team Folder")
        self.redFolderPath = QLineEdit()
        self.redFolderBrowse = QPushButton()
        self.redFolderBrowse.setText("Browse")
        self.redFolderBrowse.setEnabled(False)

        # Red folder controls container
        redContainer = QHBoxLayout()
        redContainer.addWidget(redFolderLbl)
        redContainer.addWidget(self.redFolderPath)
        redContainer.addWidget(self.redFolderBrowse)

        # Blue Folder controls
        blueFolderLbl = QLabel("Blue Team Folder")
        self.blueFolderPath = QLineEdit()
        self.blueFolderBrowse = QPushButton()
        self.blueFolderBrowse.setText("Browse")
        self.blueFolderBrowse.setEnabled(False)

        # Blue folder controls container
        blueContainer = QHBoxLayout()
        blueContainer.addWidget(blueFolderLbl)
        blueContainer.addWidget(self.blueFolderPath)
        blueContainer.addWidget(self.blueFolderBrowse)

        # Blue Folder controls
        whiteFolderLbl = QLabel("Blue Team Folder")
        self.whiteFolderPath = QLineEdit()
        self.whiteFolderBrowse = QPushButton()
        self.whiteFolderBrowse.setText("Browse")
        self.whiteFolderBrowse.setEnabled(False)

        # Blue folder controls container
        whiteContainer = QHBoxLayout()
        whiteContainer.addWidget(whiteFolderLbl)
        whiteContainer.addWidget(self.whiteFolderPath)
        whiteContainer.addWidget(self.whiteFolderBrowse)

        self.dirConfigSave = QPushButton("Save")
        

        dirViewContainer = QVBoxLayout()
        dirViewContainer.addLayout(viewLabelCon)
        dirViewContainer.addLayout(rootDirContainer)
        dirViewContainer.addLayout(redContainer)
        dirViewContainer.addLayout(blueContainer)
        dirViewContainer.addLayout(whiteContainer)
        dirViewContainer.addWidget(self.dirConfigSave)

        self.dirConfig.setLayout(dirViewContainer)

    def connect(self): 
        #TODO
        pass

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)