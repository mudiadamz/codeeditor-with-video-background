from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


class CSSSyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#0000FF"))  # Blue
        keyword_format.setFontWeight(QFont.Weight.Bold)

        property_format = QTextCharFormat()
        property_format.setForeground(QColor("#0000FF"))  # Blue

        value_format = QTextCharFormat()
        value_format.setForeground(QColor("#008000"))  # Green

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#808080"))  # Gray
        comment_format.setFontItalic(True)

        self.highlighting_rules = [
            (QRegularExpression("\\b(?:[a-zA-Z][\\w-]*|@import|@media|@keyframes|@font-face)\\b"), keyword_format),
            # Selectors and @-rules
            (QRegularExpression("\\b(?:[a-zA-Z][\\w-]*)\\s*:"), property_format),  # Properties
            (QRegularExpression(":\\s*[^\\{;]+"), value_format),  # Property values
            (QRegularExpression("/\\*.*\\*/"), comment_format)  # Comments
        ]

    def highlightBlock(self, text):
        for pattern, format in self.highlighting_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), format)
