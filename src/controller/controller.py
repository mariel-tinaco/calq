import sys
import os
from typing import Protocol


class Controller(Protocol):

    def __init__(self) -> None:
        super().__init__()


