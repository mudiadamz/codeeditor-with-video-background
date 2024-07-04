from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


class JavaScriptSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#0070C0"))  # Blue
        keyword_format.setFontWeight(QFont.Weight.Bold)

        string_format = QTextCharFormat()
        string_format.setForeground(QColor("#008000"))  # Green

        self.highlighting_rules = [
            (QRegularExpression(
                "\\b(?:function|var|let|const|if|else|for|while|do|return|break|continue|switch|case|default)\\b"),
             keyword_format),  # Keywords
            (QRegularExpression("\\b\\d+\\b"), QTextCharFormat()),  # Numbers
            (QRegularExpression("\"[^\"]*\"|\'[^\']*\'"), string_format),  # Strings
            (QRegularExpression("//.*"), QTextCharFormat().setForeground(QColor("#808080")))  # Single-line comments
        ]

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)

