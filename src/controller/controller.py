import sys
import os
import math
from PyQt5.QtWidgets import QApplication
from src.view.view import CalQMainWindow
from src.controller.utils import Mode

class Controller:

    def __init__(self) -> None:
        super().__init__()
    
    def main(self, mode : str):

        if mode == Mode.GUI.value:
            app =  QApplication(sys.argv)
            self.view = CalQMainWindow(self)
            self.view.show()
            app.exec()

    
    def compute_expression(self, expression):


        return eval(expression)