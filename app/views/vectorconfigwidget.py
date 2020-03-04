from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout,QHBoxLayout, QLabel, QPushButton, QLineEdit

class VectorConfigWidget(QWidget):
    def __init__(self, parent=None, eventManager=None):
        super(VectorConfigWidget, self).__init__(parent) 
        self.eventConfigManager = eventManager
        self.initUI()

    def initUI(self): 
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

        vectorConfigContainer = QVBoxLayout()
        vectorConfigContainer.addWidget(vectorLbl)
        vectorConfigContainer.addWidget(self.vectorsTbl)
        vectorConfigContainer.addLayout(btnContainer)

        self.setLayout(vectorConfigContainer)