import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_TeamConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QWidget, QListWidget, QStackedWidget, QTableView, QVBoxLayout, QHBoxLayout, QLabel, QPushButton, QRadioButton, QLineEdit

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
        
        self.stack = QStackedWidget(self)
        self.stack.addWidget(self.teamConfig)

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

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)