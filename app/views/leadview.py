import os
ui_dir = os.path.dirname(os.path.abspath(__file__))

from PyQt5 import uic
from PyQt5.QtWidgets import *

from .eventconfigview import EventConfigView

Ui_ChooseLead, _ = uic.loadUiType(ui_dir+r'/ui/PICK_LeadWidget.ui')

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