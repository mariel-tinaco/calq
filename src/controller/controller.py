import sys
import os
from PyQt5.QtWidgets import QApplication
from src.view.view import CalQMainWindow
from src.controller.utils import Mode


class Controller:

    def __init__(self) -> None:
        super().__init__()

    
    def main(self, mode = Mode.GUI):

        if mode == Mode.GUI:
            app =  QApplication(sys.argv)
            self.view = CalQMainWindow(self)
            self.view.show()
            app.exec()
