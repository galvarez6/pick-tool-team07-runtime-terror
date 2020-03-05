import sys
sys.path.append("../..")
from managers.vectormanager import VectorManager

from PyQt5.QtCore import Qt
from PyQt5.QtGui import QStandardItemModel, QStandardItem
from PyQt5.QtWidgets import QWidget, QTableView, QVBoxLayout,QHBoxLayout, QLabel, QPushButton, QTextEdit, QLineEdit, QHeaderView


class AddWidget(QWidget): 
    def __init__(self, 
                parent=None, 
                vectormanager=None, 
                init_name=None, 
                init_desc=None): 
        super(AddWidget, self).__init__(parent)
        self.parent = parent
        self.vectormanager = vectormanager
        self.initUI(init_name, init_desc)

    def initUI(self, init_name, init_desc): 
        namelbl = QLabel("Vector Name")
        name = QLineEdit()
        if init_name:
            name.setText(init_name)


        desclbl = QLabel("Vector Description")
        desc = QTextEdit()
        if init_desc: 
            desc.setText(init_desc)

        submit = QPushButton("Submit")
        submit.clicked.connect(lambda: self.add_submit(name, desc, init_name=init_name, init_desc=init_desc))

        container = QVBoxLayout()
        container.addWidget(namelbl)
        container.addWidget(name)
        container.addWidget(desclbl)
        container.addWidget(desc)
        container.addWidget(submit)

        self.setLayout(container)

    def add_submit(self, name, desc, init_name=None, init_desc=None):
        vec_name = name.text()
        vec_desc = desc.toPlainText()

        if init_name == None and init_desc == None: 
            print("New")
            self.vectormanager.add_vector(
                    vec_name, 
                    vec_desc)
        else:  
            if self.vectormanager.vector_exists(init_name):
                print("updating")
                vector = self.vectormanager.update_vector(init_name, vec_name, vec_desc)

        self.parent.initUI()


class VectorConfigWidget(QWidget):
    def __init__(self, parent=None, eventManager=None):
        super(VectorConfigWidget, self).__init__(parent) 
        self.eventConfigManager = eventManager
        self.vectorManager = VectorManager()
        self.initUI()

    def initUI(self): 
        vectorLbl = QLabel("Vector Configuration")

        self.vectorsTbl = QTableView()
        self.vectorsTbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)
        self.model = QStandardItemModel()
        self.model.setHorizontalHeaderLabels(['Name', 'Description'])
        self.updateTable()

        delBtn = QPushButton("Delete Vector")

        editBtn = QPushButton("Edit Vector")
        editBtn.clicked.connect(self.edit)

        addBtn = QPushButton("Add Vector")
        addBtn.clicked.connect(self.add)

        btnContainer = QHBoxLayout()
        btnContainer.addWidget(delBtn)
        btnContainer.addWidget(editBtn)
        btnContainer.addWidget(addBtn)

        vectorConfigContainer = QVBoxLayout()
        vectorConfigContainer.addWidget(vectorLbl)
        vectorConfigContainer.addWidget(self.vectorsTbl)
        vectorConfigContainer.addLayout(btnContainer)

        # This is a little hack that I am doing in order to switch between layouts in a widget.
        # Not best practice, should probably have a stack widget, but for now this seems 
        # easy enough.
        if self.layout() == None: 
            self.setLayout(vectorConfigContainer)
        else: 
            self.setNewLayout(vectorConfigContainer)


    def add(self): 
        addWidget = AddWidget(parent=self, vectormanager=self.vectorManager)
        self.setNewLayout(addWidget)

    def edit(self): 
        # TODO: There is a bug on this process
        selected = self.vectorsTbl.selectionModel()
        if selected.hasSelection(): 
            indexes = selected.selectedIndexes()
            name, desc = indexes[0].data(), indexes[1].data()
            addWidget = AddWidget(parent=self, 
                                    vectormanager=self.vectorManager,
                                    init_name=name, 
                                    init_desc=desc)
            self.setNewLayout(addWidget)
                
    def delete(self): 
        pass

    def updateTable(self): 
        vectors = self.vectorManager.get_vectors()
        for vector in vectors: 
            name = QStandardItem(vector.name)
            desc = QStandardItem(vector.description)

            self.model.appendRow([name, desc])
        self.vectorsTbl.setModel(self.model)

    def setNewLayout(self, widget): 
        QWidget().setLayout(self.layout())
        self.setLayout(widget.layout())