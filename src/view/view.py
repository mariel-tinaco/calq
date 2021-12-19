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

        self.current_mode = 0
        self.lcdNumber_value.setDigitCount(10)
        # self.lcdNumber_value.setSmallDecimalPoint()

        self.lineEdit_expression.setFocus()

        self.connect_widgets()
        self.set_default_states()

    def connect_widgets(self):
        # # Connect the expression combobox to the expression stack widget
        self.comboBox_expressions.currentIndexChanged.connect(
            lambda _ : self.stackedWidget_expr.setCurrentIndex(self.comboBox_expressions.currentIndex())
        )

        self.pushButton_calc_window.clicked.connect(lambda _ : self.change_modes(0))
        self.pushButton_eval_window.clicked.connect(lambda _ : self.change_modes(1))
        self.pushButton_func_window.clicked.connect(lambda _ : self.change_modes(2))
        self.pushButton_complex_window.clicked.connect(lambda _ : self.change_modes(3))
        self.pushButton_stat_window.clicked.connect(lambda _ : self.change_modes(4))
        self.pushButton_discrete_window.clicked.connect(lambda _ : self.change_modes(5))
        self.pushButton_matrix_window.clicked.connect(lambda _ : self.change_modes(6))
        self.pushButton_vector_window.clicked.connect(lambda _ : self.change_modes(7))

        self.pushButton_equal.clicked.connect(self.calculate)

    def set_default_states(self):
        
        self.stackedWidget_modes.setCurrentIndex(self.current_mode)

    def change_modes(self, mode_index):
        
        self.stackedWidget_modes.setCurrentIndex(mode_index)

 



    def calculate(self):
        expression = self.lineEdit_expression.text()
        result = self.controller.compute_expression(expression)
        self.lcdNumber_value.display(str(result))
    
    def keyPressEvent(self, e):
        if e.key() == QtCore.Qt.Key_Escape:
            self.close()
        elif e.key() == QtCore.Qt.Key_Enter:
            self.calculate()

    def eventFilter(self, source, event):
        if event.type() == QtCore.QEvent.KeyPress:
            if source is self.lineEdit_expression:
                if event.key() == QtCore.Qt.Key_Enter:
                    self.calculate()
                elif event.key() == QtCore.Qt.Key_Return:

                    self.calculate()

            elif source is self:
                if event.key() == QtCore.Qt.Key_Escape:
                    self.close()
        
        return super(CalQMainWindow, self).eventFilter(source, event)