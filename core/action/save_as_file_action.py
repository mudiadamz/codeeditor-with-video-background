import os

from PyQt6.QtWidgets import QFileDialog, QMessageBox


def save_as_file(main_window):
    if 0 <= main_window.tab_widget.currentIndex() < len(
            main_window.file_paths):
        index = main_window.tab_widget.currentIndex()
        try:
            content = main_window.tab_widget.widget(index).toPlainText()
            file_path, _ = QFileDialog.getSaveFileName(main_window, 'Save File')
            if file_path:
                with open(file_path, 'w', encoding='utf-8') as file:
                    file.write(content)
                main_window.file_paths[index] = file_path
                main_window.tab_widget.setTabText(index, os.path.basename(file_path))
        except Exception as e:
            QMessageBox.critical(main_window, 'Error', f"An error occurred while saving the file.py: {str(e)}")
