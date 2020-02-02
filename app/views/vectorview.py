
from .ui.uiobjects import Ui_CreateVector

from vectormanager import VectorManager

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog


class VectorDialog(QDialog): 
    def __init__(self, vecmanager): 
        super(VectorDialog,self).__init__()
        self.vecmanager = vecmanager
        self.ui = Ui_CreateVector()
        self.ui.setupUi(self)
        self.ui.addvector_btn.clicked.connect(self.add_vector)
        self.setAttribute(Qt.WA_DeleteOnClose)
        self.exec()

    def add_vector(self): 
        name = self.ui.vecname_txtbox.text()
        desc = self.ui.vecdesc_txtbox.text()
        self.vecmanager.add_vector(name, desc)
        self.done(0)