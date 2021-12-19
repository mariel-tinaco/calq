import os
import sys
from src.controller.controller import Controller
from src.controller.utils import Mode
import pathlib


if __name__ == "__main__":

    calq = Controller()
    calq.main(mode=Mode.GUI)

    