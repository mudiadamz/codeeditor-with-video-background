import os

from PyQt6.QtWidgets import QMessageBox

from core.action.save_as_file_action import save_as_file
from core.util.check_tab_save import is_tab_saved


def save_file(main_window):
    if 0 <= main_window.tab_widget.currentIndex() < len(
            main_window.file_paths):
        index = main_window.tab_widget.currentIndex()
        file_path = main_window.file_paths[index]
        if file_path:
            try:
                content = main_window.tab_widget.widget(index).toPlainText()
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)

                # Remove asterisk from tab_action.py title if content matches file content
                if is_tab_saved(main_window, index):
                    tab_title = os.path.basename(file_path)
                    main_window.tab_widget.setTabText(index, tab_title)
            except Exception as e:
                QMessageBox.critical(main_window, 'Error', f"An error occurred while saving the file: {str(e)}")
        else:
            save_as_file(main_window)  # Open save dialog for new file
