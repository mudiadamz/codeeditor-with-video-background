from PyQt6.QtGui import QAction
from PyQt6.QtWidgets import QMenu

from core.action.delete_action import delete_item
from core.action.file_copy_action import paste_item, copy_item
from core.action.find_in_files import find_in_files
from core.action.new_file_action import add_file
from core.action.new_folder_action import add_folder
from core.action.rename_action import rename_item
from core.action.replace_in_files import replace_in_files


class SidebarContextMenu(QMenu):
    def __init__(self, main_window, file_tree_view, index, parent=None):
        super().__init__()

        add_file_action = QAction('New File', main_window)
        add_file_action.triggered.connect(lambda: add_file(main_window, file_tree_view, index))
        self.addAction(add_file_action)

        add_folder_action = QAction('Add Folder', main_window)
        add_folder_action.triggered.connect(lambda: add_folder(main_window, file_tree_view, index))
        self.addAction(add_folder_action)

        # Add actions for rename, delete, copy, and paste
        rename_action = QAction('Rename', main_window)
        rename_action.triggered.connect(lambda: rename_item(main_window, file_tree_view, index))
        self.addAction(rename_action)

        delete_action = QAction('Delete', main_window)
        delete_action.triggered.connect(lambda: delete_item(main_window, file_tree_view, index))
        self.addAction(delete_action)

        copy_action = QAction('Copy', main_window)
        copy_action.triggered.connect(lambda: copy_item(main_window, file_tree_view, index))
        self.addAction(copy_action)

        paste_action = QAction('Paste', main_window)
        paste_action.triggered.connect(lambda: paste_item(main_window, file_tree_view, index))
        self.addAction(paste_action)

        find_action = QAction('Find in files', main_window)
        find_action.triggered.connect(lambda: find_in_files(main_window, file_tree_view, index))
        self.addAction(find_action)

        replace_action = QAction('Replace in files', main_window)
        replace_action.triggered.connect(lambda: replace_in_files(main_window, file_tree_view, index))
        self.addAction(replace_action)

        # Show the context menu at the clicked position
        # self.exec(file_tree_view.viewport().mapToGlobal(pos))
