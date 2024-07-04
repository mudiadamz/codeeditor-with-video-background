import os

from PyQt6.QtCore import Qt
from PyQt6.QtGui import QFileSystemModel
from PyQt6.QtWidgets import QTreeView, QWidget, QVBoxLayout

from core.action.sidebar_ctxmenu_action import sidebar_ctx_action
from core.util.file_filter_util import FileFilterProxyModel
from core.action.file_action import open_file
from core.action.setting_action import load_setting


class CustomFileTree(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        self.base_folder, window_geometry, window_state, self.open_tabs = load_setting()
        self.layout = QVBoxLayout()
        parent_folder = os.path.dirname(self.base_folder)
        file_system_model = QFileSystemModel()
        file_system_model.setRootPath(parent_folder)
        proxy_model = FileFilterProxyModel(self.base_folder)
        proxy_model.setSourceModel(file_system_model)
        file_tree_view = QTreeView()
        file_tree_view.header().setVisible(False)
        # file_tree_view.setObjectName("file_tree_view")
        file_tree_view.setModel(proxy_model)
        file_tree_view.setRootIndex(proxy_model.mapFromSource(file_system_model.index(parent_folder)))
        base_folder_index = proxy_model.mapFromSource(file_system_model.index(self.base_folder))
        file_tree_view.expand(base_folder_index)
        file_tree_view.setColumnHidden(1, True)
        file_tree_view.setColumnHidden(2, True)
        file_tree_view.setColumnHidden(3, True)

        # Connect doubleClicked signal to open_file function
        file_tree_view.doubleClicked.connect(lambda index: open_file(main_window, index, proxy_model))

        # Connect right-click signal to context menu function
        file_tree_view.setContextMenuPolicy(Qt.ContextMenuPolicy.CustomContextMenu)
        file_tree_view.customContextMenuRequested.connect(
            lambda pos: sidebar_ctx_action(self, file_tree_view, pos))

        self.layout.addWidget(file_tree_view)
        self.setLayout(self.layout)
