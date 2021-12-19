from enum import Enum, auto


class Digit(Enum):
    ZERO = 0
    ONE = 1
    TWO = 2
    THREE = 3
    FOUR = 4
    FIVE = 5
    SIX = 6
    SEVEN = 7
    EIGHT = 8
    NINE = 9

class UnaryOp(Enum):
    NEGATIVE = "-"
    PERCENT = "%"

class BinaryOp(Enum):
    ADDITION = "+"
    SUBTRACTION = "-"
    MULTIPLICATION = "×"
    DIVISION = "÷"
