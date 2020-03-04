import sys
sys.path.append("../..")
from managers.vectormanager import VectorManager

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout,QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QHeaderView

class VectorConfigWidget(QWidget):
    def __init__(self, parent=None, eventManager=None):
        super(VectorConfigWidget, self).__init__(parent) 
        self.eventConfigManager = eventManager
        self.vectorManager = VectorManager()
        self.initUI()

    def initUI(self): 
        vectorLbl = QLabel("Vector Configuration")

        self.vectorsTbl = QTableView()
        model = QStandardItemModel()
        model.setHorizontalHeaderLabels(['Name', 'Description'])
        self.vectorsTbl.setModel(model)
        self.vectorsTbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.populateTable()

        self.delBtn = QPushButton("Delete Vector")

        self.editBtn = QPushButton("Edit Vector")

        self.addBtn = QPushButton("Add Vector")
        self.addBtn.clicked.connect(self.add)

        btnContainer = QHBoxLayout()
        btnContainer.addWidget(self.delBtn)
        btnContainer.addWidget(self.editBtn)
        btnContainer.addWidget(self.addBtn)

        vectorConfigContainer = QVBoxLayout()
        vectorConfigContainer.addWidget(vectorLbl)
        vectorConfigContainer.addWidget(self.vectorsTbl)
        vectorConfigContainer.addLayout(btnContainer)

        # This is a little hack that I am doing in order to switch between layouts in a widget
        # not best implemenation, should probably have a stack widget, but for now this seems 
        # easy enough.
        if self.layout() == None: 
            self.setLayout(vectorConfigContainer)
        else: 
            QWidget().setLayout(self.layout())
            self.setLayout(vectorConfigContainer)


    def add(self): 
        namelbl = QLabel("Vector Name")
        name = QLineEdit()

        desclbl = QLabel("Vector Description")
        desc = QTextEdit()

        submit = QPushButton("Submit")
        def add_submit(instance):
            instance.vectorManager.add_vector(
                name.text(), 
                desc.toPlainText())
            instance.initUI()
            
        submit.clicked.connect(lambda: add_submit(self))

        container = QVBoxLayout()
        container.addWidget(namelbl)
        container.addWidget(name)
        container.addWidget(desclbl)
        container.addWidget(desc)
        container.addWidget(submit)

        QWidget().setLayout(self.layout())
        self.setLayout(container)

    def edit(self): 
        pass

    def delete(self): 
        pass

    def populateTable(self): 
        