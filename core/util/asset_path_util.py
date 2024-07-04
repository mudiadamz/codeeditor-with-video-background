import os
import sys


def asset_path(relative_path):
    """ Get the absolute path to the resource, works for dev and for PyInstaller """
    if relative_path.startswith('/'):
        relative_path = relative_path[1:]

    base_path = getattr(sys, '_MEIPASS', os.path.abspath("."))
    full_path = os.path.join(base_path, relative_path)
    return full_path
