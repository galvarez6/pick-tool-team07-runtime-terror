from .ui.uiobjects import Ui_DirectoryConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog

class DirConfigView(QDialog): 
    def __init__(self):
        super(DirConfigView, self).__init__() 
        self.ui = Ui_DirectoryConfig()
        self.ui.setupUi(self)
        self.setupHandler()
        self.exec_()

    def setupHandler(self): 
        self.ui.browseBtn.clicked.connect(self.browse)

    def browse(self): 
        root_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.rootDirTxtBox.setText(root_dir)