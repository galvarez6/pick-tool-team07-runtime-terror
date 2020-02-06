from .ui.uiobjects import Ui_ListGraphConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog 
from PyQt5 import QtWidgets


class ListGraphView(QDialog):
    def __init__(self, parent):
        super(ListGraphView, self).__init__(parent)
        self.parent = parent
        self.ui = Ui_ListGraphConfig()
        self.ui.setupUi(self)
        self.ui.tableWidget.setColumnCount(11)
        self.ui.tableWidget.setRowCount(50)
        self.addCheckBoxes()
        self.exec_()

    def addCheckBoxes(self):
        num = 0
        while (num < self.ui.tableWidget.columnCount()):
            check_box = QtWidgets.QCheckBox()
            self.ui.tableWidget.setCellWidget(0, num, check_box)
            num += 1
        num = 0
        while (num <= self.ui.tableWidget.rowCount()):
            check_box = QtWidgets.QCheckBox()
            self.ui.tableWidget.setCellWidget(num + 1, 0, check_box)
            num += 1

