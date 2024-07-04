from PyQt6.QtCore import Qt, QRect, pyqtSlot
from PyQt6.QtGui import QPainter, QFont, QTextCursor
from PyQt6.QtWidgets import QPlainTextEdit, QTextEdit

from core.widget.widget_line_number import WidgetLineNumber


class CodeEditor(QPlainTextEdit):
    def __init__(self, parent=None):
        super().__init__(parent)
        # self.setObjectName("NuCodeEditor")
        self.lineNumberArea = WidgetLineNumber(self)

        self.blockCountChanged.connect(self.updateLineNumberAreaWidth)
        self.updateRequest.connect(self.updateLineNumberArea)
        self.cursorPositionChanged.connect(self.highlightCurrentLine)

        self.updateLineNumberAreaWidth(0)
        self.highlightCurrentLine()

        # Set monospace font for code
        font = QFont("Consolas", 11)  # You can choose any monospace font here
        self.setFont(font)

        """Set tab size"""
        self.setTabStopDistance(4 * self.fontMetrics().horizontalAdvance(' '))

    def lineNumberAreaWidth(self):
        digits = 2
        max_num = max(1, self.blockCount())
        while max_num >= 10:
            max_num //= 10
            digits += 1
        space = 3 + self.fontMetrics().horizontalAdvance('9') * digits
        return space

    @pyqtSlot(int)
    def updateLineNumberAreaWidth(self, _):
        self.setViewportMargins(self.lineNumberAreaWidth(), 0, 0, 0)

    @pyqtSlot(QRect, int)
    def updateLineNumberArea(self, rect, dy):
        if dy:
            self.lineNumberArea.scroll(0, dy)
        else:
            self.lineNumberArea.update(0, rect.y(), self.lineNumberArea.width(), rect.height())

        if rect.contains(self.viewport().rect()):
            self.updateLineNumberAreaWidth(0)

    def resizeEvent(self, event):
        super().resizeEvent(event)
        cr = self.contentsRect()
        self.lineNumberArea.setGeometry(QRect(cr.left(), cr.top(), self.lineNumberAreaWidth(), cr.height()))

    def lineNumberAreaPaintEvent(self, event):
        painter = QPainter(self.lineNumberArea)
        block = self.firstVisibleBlock()
        block_number = block.blockNumber()
        top = int(self.blockBoundingGeometry(block).translated(self.contentOffset()).top())
        bottom = top + int(self.blockBoundingRect(block).height())

        while block.isValid() and top <= event.rect().bottom():
            if block.isVisible() and bottom >= event.rect().top():
                number = str(block_number + 1)
                painter.drawText(0, top, self.lineNumberArea.width(), self.fontMetrics().height(),
                                 Qt.AlignmentFlag.AlignRight, number)

            block = block.next()
            top = bottom
            bottom = top + int(self.blockBoundingRect(block).height())
            block_number += 1

    def highlightCurrentLine(self):
        extra_selections = []

        if not self.isReadOnly():
            selection = QTextEdit.ExtraSelection()
            selection.cursor = self.textCursor()
            selection.cursor.clearSelection()
            extra_selections.append(selection)

        self.setExtraSelections(extra_selections)

    def mousePressEvent(self, event):
        super().mousePressEvent(event)
        # cursor = self.cursorForPosition(event.pos())
        # cursor.select(QTextCursor.SelectionType.WordUnderCursor)
        # self.setTextCursor(cursor)

    def keyPressEvent(self, event):
        if event.key() == Qt.Key.Key_Return:  # Check if Enter key is pressed
            cursor = self.textCursor()
            cursor.movePosition(QTextCursor.MoveOperation.StartOfLine)  # Move cursor to start of line
            cursor.movePosition(QTextCursor.MoveOperation.EndOfLine,
                                QTextCursor.MoveMode.KeepAnchor)  # Select current line
            line_text = cursor.selectedText()
            indent = ''
            for char in line_text:
                if char.isspace():
                    indent += char
                else:
                    break
            self.insertPlainText('\n' + indent)  # Insert newline with the same indentation
        else:
            super().keyPressEvent(event)  # Call base class implementation for other keys
