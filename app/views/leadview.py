from .ui.uiobjects import Ui_TeamConfig

from PyQt5.QtWidgets import QDialog

from .eventconfigview import EventConfigView

class LeadView(QDialog): 
    def __init__(self, parent):
        super(LeadView, self).__init__(parent)

        self.parent = parent
        self.ui = Ui_TeamConfig()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.exec_()
    
    def connect(self): 
        if self.ui.leadRadioBtn.isChecked(): 
            self.done(0)
            ec = EventConfigView(self.parent)

    def add_connection(self): 
        # TODO: Open new dialog asking for the IP Address??
        pass

    def setupHandlers(self): 
        self.ui.connBtn.clicked.connect(self.connect)
        self.ui.addConnBtn.clicked.connect(self.add_connection)