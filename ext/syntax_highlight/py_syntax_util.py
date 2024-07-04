from PyQt6.QtCore import QRegularExpression
from PyQt6.QtGui import QColor, QTextCharFormat, QFont, QSyntaxHighlighter


class PySyntaxHighlighter(QSyntaxHighlighter):
    def __init__(self, parent=None):
        super().__init__(parent)

        self.highlight_rules = []

        keyword_format = QTextCharFormat()
        keyword_format.setForeground(QColor("#569CD6"))
        keyword_format.setFontWeight(QFont.Weight.Bold)
        keywords = [
            "and", "as", "assert", "break", "class", "continue", "def", "del", "elif",
            "else", "except", "finally", "for", "from", "global", "if", "import", "in",
            "is", "lambda", "nonlocal", "not", "or", "pass", "raise", "return", "try",
            "while", "with", "yield", "True", "False", "None"
        ]
        self.highlight_rules.extend([(r"\b%s\b" % keyword, keyword_format) for keyword in keywords])

        class_format = QTextCharFormat()
        class_format.setForeground(QColor("#4EC9B0"))
        self.highlight_rules.append((r"\b[A-Z][a-zA-Z0-9_]*\b", class_format))

        function_format = QTextCharFormat()
        function_format.setForeground(QColor("#DCDCAA"))
        self.highlight_rules.append((r"\b[a-zA-Z_][a-zA-Z0-9_]*\s*(?=\()", function_format))

        quotation_format = QTextCharFormat()
        quotation_format.setForeground(QColor("#D69D85"))
        self.highlight_rules.append((r'".*?"', quotation_format))
        self.highlight_rules.append((r"'.*?'", quotation_format))

        comment_format = QTextCharFormat()
        comment_format.setForeground(QColor("#6A9955"))
        self.highlight_rules.append((r"#[^\n]*", comment_format))

    def highlightBlock(self, text):
        for pattern, char_format in self.highlight_rules:
            expression = QRegularExpression(pattern)
            match_iterator = expression.globalMatch(text)
            while match_iterator.hasNext():
                match = match_iterator.next()
                self.setFormat(match.capturedStart(), match.capturedLength(), char_format)
