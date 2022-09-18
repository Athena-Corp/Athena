import importlib
import os


def load_modules():
    modules = os.listdir('modules')
    for module in modules:
        importlib.import_module('modules.' + module.replace('.py', ''))

    return len(modules)
