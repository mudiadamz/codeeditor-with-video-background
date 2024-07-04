from PyQt6.QtCore import Qt
from PyQt6.QtWidgets import QSplitter, QVBoxLayout, QWidget, QHBoxLayout, QSpacerItem, QSizePolicy, QPushButton


class MainBar(QSplitter):
    def __init__(self, main_window, custom_file_tree, parent=None):
        super().__init__(parent)
        """ Right pane """
        right_pane = QVBoxLayout()
        right_pane.setSpacing(0)
        widget_right_pane = QWidget()
        editor_bottom = QWidget()
        editor_bottom_layout = QHBoxLayout()
        editor_bottom_layout.setSpacing(20)

        # Add a stretchable spacer item to push the label to the right
        spacer_item = QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        editor_bottom_layout.addItem(spacer_item)

        # Encoding
        editor_bottom_layout.addWidget(main_window.label_encoding)

        # Tab size
        editor_bottom_layout.addWidget(main_window.label_tab_size)

        editor_bottom.setLayout(editor_bottom_layout)
        right_pane.addWidget(main_window.tab_widget)
        right_pane.addWidget(editor_bottom)
        widget_right_pane.setLayout(right_pane)

        """ Left pane """
        self.addWidget(custom_file_tree)

        """ Right pane """
        self.addWidget(widget_right_pane)

        """ Splitter settings """
        self.setSizes([200, 600])
        self.setOrientation(Qt.Orientation.Horizontal)
