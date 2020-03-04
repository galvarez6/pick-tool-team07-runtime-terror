import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QListWidget, QStackedWidget, QTableView, QVBoxLayout,\
                            QHBoxLayout, QLabel, QPushButton, QRadioButton, QLineEdit, QDateTimeEdit, QFileDialog

class ProjectConfigView(QDialog): 
    def __init__(self, parent):
        super(ProjectConfigView, self).__init__(parent)
        self.initUI()

    def initUI(self): 
        self.resize(700,500)
        self.teamConfig = QWidget()
        self.dirConfig = QWidget()
        self.eventConfig = QWidget()
        self.vectorConfig = QWidget()

        self.teamConfigSetup()
        self.dirConfigSetup()
        self.eventConfigSetup()
        self.vectorConfigSetup()
        
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamConfig)
        self.stack.addWidget(self.dirConfig)
        self.stack.addWidget(self.eventConfig)
        self.stack.addWidget(self.vectorConfig)


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
        self.rootDirPath.setReadOnly(True)
        self.rootDirBrowse = QPushButton()
        self.rootDirBrowse.setText("Browse")
        self.rootDirBrowse.clicked.connect(self.openDirectory)
        

        # Root Directory controls container
        rootDirContainer = QHBoxLayout()
        rootDirContainer.addWidget(self.rootDirPath)
        rootDirContainer.addWidget(self.rootDirBrowse)

        # Red Folder controls
        redFolderLbl = QLabel("Red Team Folder")
        self.redFolderPath = QLineEdit()
        self.redFolderPath.setReadOnly(True)
        self.redFolderBrowse = QPushButton()
        self.redFolderBrowse.setText("Browse")
        self.redFolderBrowse.setEnabled(False)

        # Red folder controls container
        redContainer = QHBoxLayout()
        redContainer.addWidget(self.redFolderPath)
        redContainer.addWidget(self.redFolderBrowse)

        # Blue Folder controls
        blueFolderLbl = QLabel("Blue Team Folder")
        self.blueFolderPath = QLineEdit()
        self.blueFolderPath.setReadOnly(True)
        self.blueFolderBrowse = QPushButton()
        self.blueFolderBrowse.setText("Browse")
        self.blueFolderBrowse.setEnabled(False)

        # Blue folder controls container
        blueContainer = QHBoxLayout()
        blueContainer.addWidget(self.blueFolderPath)
        blueContainer.addWidget(self.blueFolderBrowse)

        # Blue Folder controls
        whiteFolderLbl = QLabel("Blue Team Folder")
        self.whiteFolderPath = QLineEdit()
        self.whiteFolderPath.setReadOnly(True)
        self.whiteFolderBrowse = QPushButton()
        self.whiteFolderBrowse.setText("Browse")
        self.whiteFolderBrowse.setEnabled(False)

        # Blue folder controls container
        whiteContainer = QHBoxLayout()
        whiteContainer.addWidget(self.whiteFolderPath)
        whiteContainer.addWidget(self.whiteFolderBrowse)

        self.dirConfigSave = QPushButton("Save")

        dirViewContainer = QVBoxLayout()
        dirViewContainer.addLayout(viewLabelCon)
        dirViewContainer.addWidget(rootDirLbl)
        dirViewContainer.addLayout(rootDirContainer)
        dirViewContainer.addWidget(redFolderLbl)
        dirViewContainer.addLayout(redContainer)
        dirViewContainer.addWidget(blueFolderLbl)
        dirViewContainer.addLayout(blueContainer)
        dirViewContainer.addWidget(whiteFolderLbl)
        dirViewContainer.addLayout(whiteContainer)
        dirViewContainer.addWidget(self.dirConfigSave)

        self.dirConfig.setLayout(dirViewContainer)

    def eventConfigSetup(self):
        self.viewLabel = QLabel()
        self.viewLabel.setText("Event Configuration")
        self.viewLabel.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

        self.eventNameLbl = QLabel()
        self.eventNameLbl.setText("Event Name")
        self.eventName = QLineEdit()

        self.eventDescriptionLbl = QLabel()
        self.eventDescriptionLbl.setText("Event Description")
        self.eventDescription = QLineEdit()

        self.startTimeLbl = QLabel()
        self.startTimeLbl.setText("Start Date and Time")
        self.startTime = QDateTimeEdit()

        self.endTimeLbl = QLabel()
        self.endTimeLbl.setText("End Date and Time")
        self.endTime = QDateTimeEdit()

        self.saveEventBtn = QPushButton()
        self.saveEventBtn.setText("Save Event") 

        self.eventConfigContainer = QVBoxLayout()
        self.eventConfigContainer.addWidget(self.viewLabel)
        self.eventConfigContainer.addWidget(self.eventNameLbl)
        self.eventConfigContainer.addWidget(self.eventName)
        self.eventConfigContainer.addWidget(self.eventDescriptionLbl)
        self.eventConfigContainer.addWidget(self.eventDescription)
        self.eventConfigContainer.addWidget(self.startTimeLbl)
        self.eventConfigContainer.addWidget(self.startTime)
        self.eventConfigContainer.addWidget(self.endTimeLbl)
        self.eventConfigContainer.addWidget(self.endTime)
        self.eventConfigContainer.addWidget(self.saveEventBtn)

        self.eventConfig.setLayout(self.eventConfigContainer)

    def vectorConfigSetup(self): 
        vectorLbl = QLabel("Vector Configuration")

        self.vectorsTbl = QTableView()

        self.delBtn = QPushButton()
        self.delBtn.setText("Delete Vector")

        self.editBtn = QPushButton()
        self.editBtn.setText("Edit Vector")

        self.addBtn = QPushButton()
        self.addBtn.setText("Add Vector")

        btnContainer = QHBoxLayout()
        btnContainer.addWidget(self.delBtn)
        btnContainer.addWidget(self.editBtn)
        btnContainer.addWidget(self.addBtn)

        self.submitBtn = QPushButton()
        self.submitBtn.setText("Submit")

        vectorConfigContainer = QVBoxLayout()
        vectorConfigContainer.addWidget(vectorLbl)
        vectorConfigContainer.addWidget(self.vectorsTbl)
        vectorConfigContainer.addLayout(btnContainer)
        vectorConfigContainer.addWidget(self.submitBtn)

        self.vectorConfig.setLayout(vectorConfigContainer)

    def openDirectory(self):
        root_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.rootDirPath.setText(root_dir)
        self.redFolderBrowse.setEnabled(True)
        self.blueFolderBrowse.setEnabled(True)
        self.whiteFolderBrowse.setEnabled(True)
        

    def connect(self): 
        #TODO
        pass
        #self.eventConfigSetup()

    # def setupHandlers(self): 
    #     self.ui.connBtn.clicked.connect(self.connect)

