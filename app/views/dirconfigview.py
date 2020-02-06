import sys
sys.path.append("..")
from eventconfigmanager import EventConfigManager

from .ui.uiobjects import Ui_DirectoryConfig

from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QDialog, QFileDialog

class DirConfigView(QDialog): 
    def __init__(self, parent):
        super(DirConfigView, self).__init__(parent)
        self.parent = parent 
        self.ui = Ui_DirectoryConfig()
        self.ui.setupUi(self)
        self.setupHandler()
        self.exec_()

    def setupHandler(self): 
        self.ui.browseBtn.clicked.connect(self.browse)
        self.ui.startIngestionBtn.clicked.connect(self.startIngestion)

    def browse(self): 
        root_dir = str(QFileDialog.getExistingDirectory(self, "Select Directory"))
        self.ui.rootDirTxtBox.setText(root_dir)
    
    def startIngestion(self):
        rootDir = self.ui.rootDirTxtBox.text()
        red = self.ui.redFolderTxtBox.text()
        blue = self.ui.blueFolderTxtBox.text()
        white = self.ui.whiteFolderTxtBox.text()
        EventConfigManager.get_instance().setDirAttributes(rootDir, red, blue, white)
        self.parent.new_project()
        self.done(0) 