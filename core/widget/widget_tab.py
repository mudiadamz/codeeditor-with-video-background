from PyQt6.QtCore import Qt
from PyQt6.QtGui import QWheelEvent, QKeySequence, QShortcut, QAction
from PyQt6.QtWidgets import QTabWidget, QPlainTextEdit, QWidget, QMenu

from core.action.tab_action import close_tab


class ZoomQTabWidget(QTabWidget):
    def __init__(self, main_window, parent=None):
        super().__init__()

        self.setTabsClosable(True)
        self.tabCloseRequested.connect(lambda index: close_tab(main_window, index))

        # Create shortcuts for zooming
        zoom_in_shortcut = QShortcut(QKeySequence("Ctrl++"), self)
        zoom_in_shortcut.activated.connect(self.zoom_in)

        zoom_out_shortcut = QShortcut(QKeySequence("Ctrl+-"), self)
        zoom_out_shortcut.activated.connect(self.zoom_out)

    def zoom_in(self):
        for index in range(self.count()):
            widget = self.widget(index)
            if isinstance(widget, QWidget):
                self.zoom_widget(widget, 1)

    def zoom_out(self):
        for index in range(self.count()):
            widget = self.widget(index)
            if isinstance(widget, QWidget):
                self.zoom_widget(widget, -1)

    def zoom_widget(self, widget, delta):
        if isinstance(widget, QPlainTextEdit):
            current_font = widget.font()
            current_font_size = current_font.pointSizeF()
            new_font_size = current_font_size + delta
            if new_font_size > 0:
                new_font = current_font
                new_font.setPointSizeF(new_font_size)
                widget.setFont(new_font)

    def wheelEvent(self, event: QWheelEvent):
        if event.modifiers() & Qt.KeyboardModifier.ControlModifier:
            # Ignore the wheel event when Ctrl key is held down
            event.ignore()
            # Perform zooming using Ctrl+Wheel
            if event.angleDelta().y() > 0:
                self.zoom_in()
            else:
                self.zoom_out()
        else:
            super().wheelEvent(event)

    def contextMenuEvent(self, event):
        try:
            context_menu = QMenu(self)
            close_action = QAction("Close Tab", self)
            close_action.triggered.connect(self.closeCurrentTab)
            context_menu.addAction(close_action)

            close_others_action = QAction("Close Other Tabs", self)
            close_others_action.triggered.connect(self.closeOtherTabs)
            context_menu.addAction(close_others_action)

            context_menu.exec(event.globalPos())
        except Exception as e:
            print(e)

    def closeCurrentTab(self):
        if self.currentIndex() != -1:
            self.removeTab(self.currentIndex())

    def closeOtherTabs(self):
        current_index = self.currentIndex()
        for i in range(self.count()):
            if i != current_index:
                self.removeTab(i)
