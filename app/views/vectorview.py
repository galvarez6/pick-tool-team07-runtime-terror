import sys
sys.path.append("..") # This is to get VectorManager in scope
from vectormanager import VectorManager

from PyQt5 import QtCore
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

from .ui.uiobjects import Ui_VectorConfig
from .vectordefview import VectorDefDialog

class VectorDialog(QDialog): 
    def __init__(self): 
        super(VectorDialog,self).__init__()
        self.vecmanager = VectorManager.get_instance()
        self.ui = Ui_VectorConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.exec()

    def setupHandlers(self): 
        self.ui.delBtn.clicked.connect(self.del_vector)
        self.ui.addBtn.clicked.connect(self.add_vector)
        self.ui.editBtn.clicked.connect(self.edit_vector)
        self.ui.submitBtn.clicked.connect(self.submit)

    def add_vector(self): 
        # TODO: Create a new dialog asking for name and description of vector
        VectorDefDialog(self)
        model = QStandardItemModel(0,2)
        model.setHorizontalHeaderLabels(
            ['Name', 
            'Description']
        )
        for vector in self.vecmanager.get_vectors(): 
            name_item = QStandardItem(vector.name)
            desc_item = QStandardItem(vector.description)

            model.appendRow([name_item, desc_item])
        self.ui.vectorTbl.setModel(model)
        self.ui.vectorTbl.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def del_vector(self): 
        index_list = []                                                          
        for model_index in self.vectorTbl.selectionModel().selectedRows():       
            index = QtCore.QPersistentModelIndex(model_index)         
            index_list.append(index)                                             

        for index in index_list:                                      
            self.vectorTbl.removeRow(index.row()) 

    def edit_vector(self): 
        selected_rows = self.vectorTbl.selectionModel().selectedRows()

    def submit(self): 
        # TODO: Next view after this one
        pass