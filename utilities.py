"""
Utilities
"""
import constants

def list_models():
    """
    List all models
    """
    for model in constants.Model:
        print(model.name, model.value)

def list_intefaces():
    """
    List all interfaces
    """
    for interface in constants.Interface:
        print(interface.name, interface.value)
