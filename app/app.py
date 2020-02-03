from PyQt5 import QtWidgets

from views.mainwindow import MainWindow   

if __name__ == '__main__': 
    import sys
    app = QtWidgets.QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())