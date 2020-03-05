from PyQt5 import QtWidgets

from app.views.mainwindow import MainWindow
from app.views.processingview import ProcessingView

if __name__ == '__main__': 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())