import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_TeamConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QListWidget, QStackedWidget, QTableView, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QLineEdit, QDateTimeEdit

from .eventconfigview import EventConfigView

class ProjectConfigView(QDialog): 
    def __init__(self, parent):
        super(ProjectConfigView, self).__init__(parent)
        self.initUI()

    def initUI(self): 
        self.viewList = QListWidget()
        self.viewList.insertItem(0, "Team Configuration")
        self.viewList.insertItem(1, "Directory Configuration")
        self.viewList.insertItem(2, "Event Configuration")
        self.viewList.insertItem(3, "Vector Configuration")

        self.teamConfig = QWidget()
        self.dirConfig = QWidget()
        self.eventConfig = QWidget()
        self.vectorConfig = QWidget()

        self.teamConfigSetup()
        self.eventConfigSetup()
        
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamConfig)
        self.stack.addWidget(self.eventConfig)

        viewContainer = QHBoxLayout(self)
        viewContainer.addWidget(self.viewList, 30)
        viewContainer.addWidget(self.stack, 60)

        self.setLayout(viewContainer)
        self.exec_()
    
    def teamConfigSetup(self): 
        self.viewLabel = QLabel()
        self.viewLabel.setText("Team Configuration")
        self.viewLabel.setAlignment(Qt.AlignHCenter|Qt.AlignVCenter)

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


        self.teamViewContainer = QVBoxLayout()
        self.teamViewContainer.addWidget(self.viewLabel)
        self.teamViewContainer.addWidget(self.leadRbtn)
        self.teamViewContainer.addLayout(self.ipContainer)
        self.teamViewContainer.addWidget(self.connectionsLbl)
        self.teamViewContainer.addWidget(self.connectionsView)
        self.teamViewContainer.addWidget(self.connectBtn)

        self.teamConfig.setLayout(self.teamViewContainer)

    def connect(self): 
        #TODO
        pass
        #self.eventConfigSetup()

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)

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



