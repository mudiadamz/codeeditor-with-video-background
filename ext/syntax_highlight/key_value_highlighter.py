from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


class KeyValueHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        key_format = QTextCharFormat()
        key_format.setForeground(QColor("#800000"))  # Red
        key_format.setFontWeight(QFont.Weight.Bold)

        value_format = QTextCharFormat()
        value_format.setForeground(QColor("#008000"))  # Green

        self.highlighting_rules = [
            (QRegularExpression("\"[^\"]*\"\\s*:"), key_format),  # Key: (enclosed in quotes)
            (QRegularExpression("[a-zA-Z]\\w*\\s*:"), key_format),  # Key: (without quotes)
            (QRegularExpression("\\bnull\\b"), value_format),  # Null value
            (QRegularExpression("\\b(true|false)\\b"), value_format),  # Boolean value
            (QRegularExpression("\\b\\d+(\\.\\d+)?\\b"), value_format),  # Number value
            (QRegularExpression("\"[^\"]*\""), value_format)  # String value
        ]

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
