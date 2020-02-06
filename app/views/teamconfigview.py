import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_TeamConfig

from PyQt5.QtWidgets import QDialog

from .eventconfigview import EventConfigView

class TeamConfigView(QDialog): 
    def __init__(self, parent):
        super(TeamConfigView, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_TeamConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.exec_()
    
    def connect(self): 
        if self.ui.leadRadioBtn.isChecked(): 
            ip = self.ui.leadIPTxtBox.text()
            # TODO: Get the total connections
            EventConfigManager.get_instance().setTeamAttributes(True, ip, 0)
            ec = EventConfigView(self.parent)
            self.done(0)

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)