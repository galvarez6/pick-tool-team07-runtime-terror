import sys
sys.path.append("..") # This is to get VectorManager in scope

from .ui.uiobjects import Ui_EventConfig, Ui_CreateVector

from vectormanager import VectorManager

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class VectorDialog(QDialog): 
    def __init__(self, vecmanager): 
        super(VectorDialog,self).__init__()
        self.ui = Ui_CreateVector()
        self.ui.setupUi(self)
        self.ui.addvector_btn.clicked.connect(lambda: self.add_vector(vecmanager))
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.exec()

    def add_vector(self, vecmanager): 
        name = self.ui.vecname_txtbox.text()
        desc = self.ui.vecdesc_txtbox.text()
        start = self.ui.start_dt.dateTime().toPyDateTime()
        end = self.ui.end_dt.dateTime().toPyDateTime()
        vecmanager.add_vector(name, desc, start, end)
        self.reject()

class EventConfigView(QWidget):
    def __init__(self, parent):
        super(EventConfigView, self).__init__(parent)
        self.vector_manager = VectorManager()
        self.parent = parent
        self.ui = Ui_EventConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        parent.setCentralWidget(self)  

    def update_listview(self):
        model = QStandardItemModel(0,4)
        model.setHorizontalHeaderLabels(
            ['Name', 
            'Description', 
            'Start Date and Time', 
            'End Date and Time']
        )
        for vector in self.vector_manager.get_vectors(): 
            name_item = QStandardItem(vector.name)
            desc_item = QStandardItem(vector.description)
            
            time_format = "%m/%d/%Y, %H:%M:%S"
            start_item = QStandardItem(vector.startdatetime.strftime(time_format))
            end_item = QStandardItem(vector.enddatetime.strftime(time_format))

            model.appendRow([name_item, desc_item, start_item, end_item])
        self.ui.vector_tblview.setModel(model)
        self.ui.vector_tblview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setupHandlers(self): 
        self.ui.browse_btn.clicked.connect(self.get_dir)
        self.ui.insertvector_btn.clicked.connect(self.create_vector)

    def get_dir(self):
        hdir = QFileself.getExistingDirectory(self, "Select Directory")
        self.ui.hdloc_textbox.setText(str(hdir))

    def create_vector(self):
        dialog = VectorDialog(self.vector_manager)
        self.update_listview()