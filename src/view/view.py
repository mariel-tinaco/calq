import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets, QtCore, QtGui, uic

UI_PATH = Path("src/view/resources/calq.ui")


class CalQMainWindow(QtWidgets.QMainWindow):

    def __init__(self, controller) -> None:
        super(CalQMainWindow, self).__init__()
        self.controller = controller
        uic.loadUi(UI_PATH, self)

        self.initialize()

    def initialize(self):

        self.connect_widgets()
        self.set_default_states()

    def connect_widgets(self):
        # # Connect the expression combobox to the expression stack widget
        self.comboBox_expressions.currentIndexChanged.connect(
            lambda _ : self.stackedWidget_expr.setCurrentIndex(self.comboBox_expressions.currentIndex())
        )

    def set_default_states(self):
        
        self.stackedWidget_modes.setCurrentIndex(0)