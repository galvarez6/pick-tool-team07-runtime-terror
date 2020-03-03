from PyQt5.QtWidgets import QWidget, QFrame, QGridLayout, QHBoxLayout, QVBoxLayout, QTableView,\
                            QTableWidget, QTabWidget, QListWidget, QLineEdit, QComboBox, QSpacerItem, QSizePolicy, QAction

class ProcessingView(QWidget):
    def __init__(self, parent=None): 
        super(QWidget, self).__init__(parent)
        self.initUI()

    def initUI(self):
        # TODO: LOG PROCESSING VIEW
         