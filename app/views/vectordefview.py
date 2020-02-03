import sys
sys.path.append("..") 
from vectormanager import VectorManager

from .ui.uiobjects import Ui_VectorDef

from PyQt5.QtWidgets import QDialog

class VectorDefDialog(QDialog): 
    def __init__(self, parent): 
        super(VectorDefDialog, self).__init__(parent)
        self.vecmanager = VectorManager.get_instance()
        self.ui = Ui_VectorDef()
        self.ui.setupUi(self)
        self.setupHandlers()
        self.exec_()

    def setupHandlers(self): 
        self.ui.submitBtn.clicked.connect(self.submit)

    def submit(self): 
        name = self.ui.nameTxtBox.text()
        desc = self.ui.descTxtBox.text()
        self.vecmanager.add_vector(name, desc)
        self.done(0)