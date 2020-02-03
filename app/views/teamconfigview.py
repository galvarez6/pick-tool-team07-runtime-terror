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
            self.done(0)
            ec = EventConfigView(self.parent)

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)