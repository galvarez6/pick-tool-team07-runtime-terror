from .ui.uiobjects import Ui_ListGraphConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog


class ListGraphView(QDialog):
    def __init__(self, parent):
        super(ListGraphView, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ListGraphConfig()
        self.ui.setupUi(self)
        self.exec_()