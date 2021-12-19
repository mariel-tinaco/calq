import os
import sys
from src.controller.controller import Controller
from src.controller.utils import Mode
import pathlib


if __name__ == "__main__":
    # # Controller Modes:
    # #     g - GUI mode
    # #     t - Terminal mode
    # #     s - Script mode

    calq = Controller()
    calq.main(mode="g")

    