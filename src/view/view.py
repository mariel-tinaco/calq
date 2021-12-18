import sys
import os
from pathlib import Path
from PyQt5 import QtWidgets, QtCore, QtGui


class CalQMainWindow(QtWidgets.QMainWindow):

    def __init__(self) -> None:
        super().__init__()

