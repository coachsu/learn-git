"""
Constant definition
"""
from enum import Enum

class Model(Enum):
    """
    Model
    """
    X100 = 0
    X200 = 1
    X200 = 2
    X300 = 3

class Interface(Enum):
    """
    Interface
    """
    RS232 = 0
    RS485 = 1
    ETHERNET = 2
