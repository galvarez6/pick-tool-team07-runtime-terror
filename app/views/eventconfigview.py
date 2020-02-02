
import sys
sys.path.append("..") # This is to get VectorManager in scope

from .ui.uiobjects import Ui_EventConfig, Ui_CreateVector

from vectormanager import VectorManager

from .vectorview import VectorDialog

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QDialog, QHeaderView
from PyQt5.QtGui import QStandardItemModel, QStandardItem

class EventConfigView(QDialog):
    def __init__(self, parent):
        super(EventConfigView, self).__init__(parent)
        self.vector_manager = VectorManager()
        self.parent = parent
        self.ui = Ui_EventConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.exec_()
        # parent.setCentralWidget(self)  

    def update_listview(self):
        model = QStandardItemModel(0,2)
        model.setHorizontalHeaderLabels(
            ['Name', 
            'Description']
        )
        for vector in self.vector_manager.get_vectors(): 
            name_item = QStandardItem(vector.name)
            desc_item = QStandardItem(vector.description)

            model.appendRow([name_item, desc_item])
        self.ui.vector_tblview.setModel(model)
        self.ui.vector_tblview.horizontalHeader().setSectionResizeMode(QHeaderView.Stretch)

    def setupHandlers(self): 
        self.ui.saveEvntBtn.clicked.connect(self.saveEvent)

    def saveEvent(self): 
        name = self.ui.eventNameTxtBox.text()
        desc = self.ui.eventDescTxtBox.text()
        start = self.ui.startTime.dateTime()
        end = self.ui.endTime.dateTime()
        print([start, end])
        # TODO: Move to next dialog and save the event configuration