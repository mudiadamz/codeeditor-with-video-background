from PyQt6.QtCore import Qt, QSettings
from PyQt6.QtGui import QShortcut, QKeySequence
from PyQt6.QtWidgets import (QMainWindow, QWidget, QVBoxLayout, QFileDialog, QPushButton)

from core.action.save_file_action import save_file
from core.action.setting_action import save_setting, load_setting
from core.action.tab_action import add_tab
from core.action.close_shortcut import handle_close_shortcut
from core.widget.widget_sidebar import CustomFileTree
from core.widget.widget_main_bar import MainBar
from core.widget.widget_tab import ZoomQTabWidget
from core.widget.widget_top_bar import CustomTopBar


class MainWindow(QMainWindow):
    file_paths = []

    def __init__(self):
        super().__init__()
        self.base_folder, window_geometry, window_state, self.open_tabs = load_setting()
        self.setWindowFlags(Qt.WindowType.FramelessWindowHint)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout(self.central_widget)
        self.layout.setContentsMargins(0, 0, 0, 0)
        self.layout.setSpacing(0)

        self.custom_title_bar = CustomTopBar(self)
        self.layout.addWidget(self.custom_title_bar)

        self.tab_widget = ZoomQTabWidget(self)
        self.custom_file_tree = CustomFileTree(self)
        self.label_encoding = QPushButton('Encoding')
        self.label_tab_size = QPushButton('Tab size')
        self.main_bar = MainBar(self, self.custom_file_tree)
        self.layout.addWidget(self.main_bar)

        self.setLayout(self.layout)
        self.setWindowTitle("XPrime Editor")
        self.setGeometry(100, 100, 800, 600)

        # Create a shortcut for Ctrl+S (save)
        save_shortcut = QShortcut(QKeySequence.StandardKey.Save, self)
        save_shortcut.activated.connect(lambda: save_file(self))
        # Create a shortcut for Ctrl+T Ctrl+N (new tab)
        new_shortcut = QShortcut(QKeySequence.StandardKey.New, self)
        new_shortcut.activated.connect(lambda: add_tab(self))
        newt_shortcut = QShortcut(QKeySequence("Ctrl+t"), self)
        newt_shortcut.activated.connect(lambda: add_tab(self))
        # Close tab Ctrl+W
        newt_shortcut = QShortcut(QKeySequence("Ctrl+w"), self)
        newt_shortcut.activated.connect(lambda : handle_close_shortcut(self))

        # Restore open tabs
        for tab_path in self.open_tabs:
            add_tab(self, file_path=tab_path)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        self.custom_title_bar.setFixedWidth(self.width())

    def reopen_window(self):
        my_settings = QSettings("YourCompany", "YourApp")
        new_base_folder = QFileDialog.getExistingDirectory(self, 'Select Folder')
        my_settings.setValue("base_folder", new_base_folder)
        if new_base_folder:
            new_window = MainWindow()
            new_window.show()
            new_window.showMaximized()

    def closeEvent(self, event):
        try:
            open_tabs = [self.tab_widget.widget(index).file_path for index in range(self.tab_widget.count())]
            save_setting(self.base_folder, self, open_tabs)
            event.accept()
        except Exception as e:
            print(e)
