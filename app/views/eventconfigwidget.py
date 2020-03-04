from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout,QHBoxLayout, QLabel, QPushButton, QLineEdit, QDateTimeEdit

class EventConfigWidget(QWidget):
    def __init__(self, parent=None, eventManager=None): 
        super(EventConfigWidget, self).__init__(parent) 
        self.eventConfigManager = eventManager
        self.initUI()

    def initUI(self): 
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

        saveBtn = QPushButton("Save")

        eventConfigContainer = QVBoxLayout()
        eventConfigContainer.addWidget(self.viewLabel)
        eventConfigContainer.addWidget(self.eventNameLbl)
        eventConfigContainer.addWidget(self.eventName)
        eventConfigContainer.addWidget(self.eventDescriptionLbl)
        eventConfigContainer.addWidget(self.eventDescription)
        eventConfigContainer.addWidget(self.startTimeLbl)
        eventConfigContainer.addWidget(self.startTime)
        eventConfigContainer.addWidget(self.endTimeLbl)
        eventConfigContainer.addWidget(self.endTime)
        eventConfigContainer.addWidget(saveBtn)

        self.setLayout(eventConfigContainer)