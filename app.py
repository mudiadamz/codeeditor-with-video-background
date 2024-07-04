"""
Cool code editor
"""
import sys

from PyQt6.QtGui import QIcon
from PyQt6.QtWidgets import (QApplication)

from core.util.app_style import app_style
from core.widget.widget_main_window import MainWindow
from core.util.asset_path_util import asset_path

if __name__ == "__main__":
    app = QApplication(sys.argv)
    app.setStyle('Fusion')
    path_icon = asset_path("core/assets/xicon.ico")
    app.setWindowIcon(QIcon(path_icon))
    main_win = MainWindow()
    app_style(app)
    main_win.show()
    main_win.showMaximized()
    sys.exit(app.exec())
