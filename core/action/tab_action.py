import os
import traceback

from PyQt6.QtWidgets import QMessageBox

from core.action.save_file_action import save_file
from ext.syntax_highlight.css_highlighter import CSSSyntaxHighlighter
from ext.syntax_highlight.html_highliter import HTMLSyntaxHighlighter
from ext.syntax_highlight.js_highlighter import JavaScriptSyntaxHighlighter
from ext.syntax_highlight.key_value_highlighter import KeyValueHighlighter
from core.util.check_tab_save import is_tab_saved
from core.util.detect_encoding import detect_file_encoding
from core.util.detect_tab_size import detect_tab_size
from ext.syntax_highlight.py_syntax_util import PySyntaxHighlighter
from core.util.file_ext import get_file_extension
from core.widget.widget_editor import CodeEditor


def close_tab(main_window, index):
    if 0 <= index < main_window.tab_widget.count():
        try:
            if not is_tab_saved(main_window, index):
                confirm_dialog = QMessageBox.question(main_window, 'Confirm Close',
                                                      'Do you want to save changes before closing?',
                                                      QMessageBox.StandardButton.Save | QMessageBox.StandardButton.Discard | QMessageBox.StandardButton.Cancel)
                if confirm_dialog == QMessageBox.StandardButton.Save:
                    save_file(main_window)
                    main_window.tab_widget.removeTab(index)
                    del main_window.file_paths[index]
                elif confirm_dialog == QMessageBox.StandardButton.Discard:
                    main_window.tab_widget.removeTab(index)
                    del main_window.file_paths[index]
            else:
                main_window.tab_widget.removeTab(index)
                del main_window.file_paths[index]
        except Exception as e:
            print(e)
            QMessageBox.critical(main_window, 'Error', f"An error occurred while closing the tab: {str(e)}")


def add_tab(main_window, content=None, file_path=None):
    try:
        encoding = detect_file_encoding(file_path)
        tab_size, uses_tabs = detect_tab_size(file_path)
        file_ext = get_file_extension(file_path)
        if content is None and file_path is not None:
            # If the file_action.py is not open, add a new tab_action.py with the file_action.py content
            with open(file_path, 'r') as file:
                content = file.read()

        text_edit = CodeEditor(main_window)
        text_edit.file_path = file_path
        text_edit.setPlainText(content)
        text_edit.document().setModified(False)
        text_edit.textChanged.connect(lambda: update_tab_text(main_window))
        tab_title = os.path.basename(file_path) if file_path else "Untitled"
        index = main_window.tab_widget.addTab(text_edit, tab_title)
        main_window.file_paths.append(file_path)
        main_window.tab_widget.setCurrentIndex(index)

        ''' Apply syntax highlighting, default python '''
        if file_ext == "html":
            highlighter = HTMLSyntaxHighlighter(text_edit.document())
        elif file_ext == "py":
            highlighter = PySyntaxHighlighter(text_edit.document())
        elif file_ext == "js":
            highlighter = JavaScriptSyntaxHighlighter(text_edit.document())
        elif file_ext == "css":
            highlighter = CSSSyntaxHighlighter(text_edit.document())
        else:
            highlighter = KeyValueHighlighter(text_edit.document())

        main_window.highlighter = highlighter

        ''' Bottom bar '''
        main_window.label_encoding.setText(encoding)
        main_window.label_tab_size.setText(f"{tab_size} {uses_tabs}")

    except Exception as e:
        traceback.print_exc()
        QMessageBox.critical(main_window, 'Error', f"{str(e)}")


def update_tab_text(main_window):
    try:
        index = main_window.tab_widget.currentIndex()
        if 0 <= index < len(main_window.file_paths):
            text_edit = main_window.tab_widget.widget(index)
            tab_title = os.path.basename(main_window.file_paths[index]) if main_window.file_paths[index] else "Untitled"
            if text_edit.document().isModified():
                tab_title = "*" + tab_title
            main_window.tab_widget.setTabText(index, tab_title)
    except Exception as e:
        print(e)
        QMessageBox.critical(main_window, 'Error', f"An error occurred while updating tab text: {str(e)}")
