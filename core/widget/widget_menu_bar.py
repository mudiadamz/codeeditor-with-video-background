from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenuBar

from core.action.check_update import check_update
from core.action.file_action import open_file_dialog_and_open_file, new_file
from core.action.find_in_files import find_in_files
from core.action.replace_in_files import replace_in_files
from core.action.save_as_file_action import save_as_file
from core.action.save_file_action import save_file
from core.widget.dialog_about import about_dialog


class CustomMenuBar(QMenuBar):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)

        file_menu = self.addMenu('File')

        open_action = QAction('Open File', main_window)
        open_action.triggered.connect(
            lambda: open_file_dialog_and_open_file(main_window))
        file_menu.addAction(open_action)

        settings_action = QAction('Open Folder', main_window)
        settings_action.triggered.connect(lambda: main_window.reopen_window())
        file_menu.addAction(settings_action)

        new_action = QAction('New Project', main_window)
        new_action.triggered.connect(lambda: new_file(main_window))
        file_menu.addAction(new_action)

        save_action = QAction('Save', main_window)
        save_action.triggered.connect(lambda: save_file(main_window))
        file_menu.addAction(save_action)

        save_as_action = QAction('Save As', main_window)
        save_as_action.triggered.connect(lambda: save_as_file(main_window))
        file_menu.addAction(save_as_action)

        exit_action = QAction('Exit', main_window)
        exit_action.triggered.connect(main_window.close)
        file_menu.addAction(exit_action)

        find_menu = self.addMenu('Find')
        find_action = QAction('Find in files', main_window)
        find_action.triggered.connect(lambda : find_in_files(main_window))
        find_menu.addAction(find_action)

        replace_action = QAction('Replace in files', main_window)
        replace_action.triggered.connect(lambda : replace_in_files(main_window))
        find_menu.addAction(replace_action)

        help_menu = self.addMenu('Help')

        about_action = QAction('About', main_window)
        about_action.triggered.connect(lambda : about_dialog(main_window))
        help_menu.addAction(about_action)

        update_action = QAction('Check for update', main_window)
        update_action.triggered.connect(lambda : check_update(main_window))
        help_menu.addAction(update_action)


        self.set_menu_bar_styles()

    def set_menu_bar_styles(self):
        self.setStyleSheet("""
            /*QMenuBar {
                background-color: #333333;
                color: white;
            }*/
            QMenuBar::item {
                padding: 10px;
                /*background-color: #333333;*/
                color: white;
            }
            QMenuBar::item:selected {
                background-color: #555555;  /* Darker grey color for hover */
            }
            QMenuBar::item:pressed {
                background-color: #777777;  /* Even darker grey color for pressed */
            }
        """)
