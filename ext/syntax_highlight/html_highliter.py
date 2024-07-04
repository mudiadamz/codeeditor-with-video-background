from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QSyntaxHighlighter, QTextCharFormat, QColor, QFont


class HTMLSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#0070C0"))  # Blue
        keyword_format.setFontWeight(QFont.Weight.Bold)

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#008000"))  # Green

        self.highlighting_rules = [
            (QRegularExpression(
                "\\b(?:DOCTYPE|html|head|body|title|script|style|meta|link|a|img|div|p|h[1-6]|span|input|ul|button|li|table)\\b"),
             keyword_format),
            (QRegularExpression("&\\w+;"), keyword_format),  # HTML entities
            (QRegularExpression("\"[^\"]*\""), string_format)  # Text between quotes
        ]

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
