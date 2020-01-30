import os 
ui_dir = os.path.dirname(os.path.abspath(__file__))

from PyQt5 import uic

Ui_MainWindow, _ = uic.loadUiType(ui_dir+r'/PICK_App.ui')

Ui_ChooseLead, _ = uic.loadUiType(ui_dir+r'/PICK_LeadWidget.ui')

Ui_EventConfig,_ = uic.loadUiType(ui_dir+r'/PICK_ECWidget.ui') 
Ui_CreateVector, _ = uic.loadUiType(ui_dir+r'/PICK_CreateVectorWidget.ui')