from .ui.uiobjects import Ui_ChooseLead

from PyQt5 import uic
from PyQt5.QtWidgets import QWidget

from .eventconfigview import EventConfigView

class LeadView(QWidget): 
    def __init__(self, parent):
        super(LeadView, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ChooseLead()
        self.ui.setupUi(self)
        self.ui.submitBtn.clicked.connect(self.on_click)
        parent.setCentralWidget(self)
    
    def on_click(self): 
        if self.ui.yesRadioBtn.isChecked(): 
            ec = EventConfigView(self.parent)