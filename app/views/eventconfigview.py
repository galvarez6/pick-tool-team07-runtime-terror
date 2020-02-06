import sys
sys.path.append("..") # This is to get VectorManager in scope
from vectormanager import VectorManager
from eventconfigmanager import EventConfigManager

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QHeaderView

from .ui.uiobjects import Ui_EventConfig

from .vectorview import VectorDialog

class EventConfigView(QDialog):
    def __init__(self, parent):
        super(EventConfigView, self).__init__(parent)
        self.vector_manager = VectorManager.get_instance()
        self.parent = parent
        self.ui = Ui_EventConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.exec_()

    def setupHandlers(self): 
        self.ui.saveEvntBtn.clicked.connect(self.saveEvent)

    def saveEvent(self): 
        name = self.ui.eventNameTxtBox.text()
        desc = self.ui.eventDescTxtBox.text()
        start = self.ui.startTime.dateTime().toPyDateTime()
        end = self.ui.endTime.dateTime().toPyDateTime()
        EventConfigManager.get_instance().setEventAttributes(name, desc, start ,end)
        self.done(0)
        VectorDialog(self.parent)