from PyQt6.QtCore import QSize, QTimer
from PyQt6.QtGui import QPainter, QPalette, QIcon
from PyQt6.QtWidgets import (QWidget, QStyle,
                             QStyleOption, QHBoxLayout, QPushButton)

from core.util.asset_path_util import asset_path
from core.widget.widget_menu_bar import CustomMenuBar


class CustomTopBar(QWidget):
    def __init__(self, main_window, parent=None):
        super().__init__(parent)
        style = self.style()
        self.setObjectName("CustomTopBar")
        self.setFixedHeight(40)
        self.setAutoFillBackground(True)
        self.setBackgroundRole(QPalette.ColorRole.Window)

        # Horizontal Layout
        self.layout = QHBoxLayout(self)
        self.layout.setContentsMargins(0, 0, 0, 0)

        # App Title
        self.title_label = QPushButton()
        path_icon = asset_path("core/assets/xicon.ico")
        icon = QIcon(path_icon)
        self.title_label.setStyleSheet("margin-left:10px")
        self.title_label.setIcon(icon)
        self.layout.addWidget(self.title_label)

        # Menu bar
        self.custom_menu_bar = CustomMenuBar(main_window)
        self.layout.addWidget(self.custom_menu_bar)

        # Minimize icon
        self.minimize_button = QPushButton(self)
        self.minimize_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_TitleBarMinButton))
        self.minimize_button.setFixedSize(30, 30)
        self.minimize_button.mousePressEvent = self.minimize
        self.layout.addWidget(self.minimize_button)

        self.maximize_button = QPushButton(self)
        self.maximize_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_TitleBarMaxButton))
        self.maximize_button.setFixedSize(30, 30)
        self.maximize_button.clicked.connect(self.maximize)
        self.layout.addWidget(self.maximize_button)

        # Close icon
        self.close_button = QPushButton(self)
        self.close_button.setIcon(style.standardIcon(QStyle.StandardPixmap.SP_TitleBarCloseButton))
        self.close_button.setObjectName("closeButton")
        self.close_button.setFixedSize(30, 30)
        self.close_button.clicked.connect(lambda event: self.close_with_delay(event))
        self.layout.addWidget(self.close_button)

        self.set_button_styles()
        self.setLayout(self.layout)


    def minimize(self, event):
        self.window().showMinimized()

    def maximize(self):
        if self.window().isMaximized():
            self.window().showNormal()
        else:
            self.window().showMaximized()

    def close_with_delay(self, event):
        QTimer.singleShot(100, lambda: self.close(event))

    def close(self, event):
        try:
            self.window().close()
        except Exception as e:
            print(e)

    def sizeHint(self):
        return QSize(200, 40)

    def paintEvent(self, event):
        option = QStyleOption()
        option.initFrom(self)
        painter = QPainter(self)
        self.style().drawPrimitive(QStyle.PrimitiveElement.PE_Widget, option, painter, self)

    def set_button_styles(self):
        button_style = """
            QPushButton {
                border: none;
                color: white
            }
            QPushButton:hover {
                background-color: #CCCCCC;
            }
            QPushButton:pressed {
                background-color: #AAAAAA;
            }
            #closeButton:hover {
                background-color: #ff0000;
            }
        """
        self.minimize_button.setStyleSheet(button_style)
        self.maximize_button.setStyleSheet(button_style)
        self.close_button.setStyleSheet(button_style)
