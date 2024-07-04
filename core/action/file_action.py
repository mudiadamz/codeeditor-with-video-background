from PyQt6.QtCore import QSortFilterProxyModel
from PyQt6.QtWidgets import QMessageBox, QFileDialog

from core.action.tab_action import add_tab


def new_file(main_window):
    add_tab(main_window)


def open_file_editor(main_window, file_path):
    try:
        # Check if the file_action.py is already open
        existing_index = main_window.file_paths.index(file_path) if file_path in main_window.file_paths else -1
        if existing_index != -1:
            # If the file_action.py is already open, navigate to the existing tab_action.py
            main_window.tab_widget.setCurrentIndex(existing_index)
        else:
            # If the file_action.py is not open, add a new tab_action.py with the file_action.py content
            with open(file_path, 'r') as file:
                content = file.read()
            add_tab(main_window, content, file_path)
    except Exception as e:
        QMessageBox.critical(main_window, 'Error', f"An error occurred while opening the file.py: {str(e)}")


def open_file(main_window, index, file_system_model):
    try:
        # Check if the model is a proxy model
        if isinstance(file_system_model, QSortFilterProxyModel):
            # If it's a proxy model, map the proxy index to the source model index
            source_index = file_system_model.mapToSource(index)
            # Get the source model
            source_model = file_system_model.sourceModel()
        else:
            # If it's not a proxy model, use the model directly
            source_index = index
            source_model = file_system_model

        # Retrieve the file path from the source model
        file_path = source_model.filePath(source_index)

        # Check if the selected item is a file
        if file_path and not source_model.isDir(source_index):
            open_file_editor(main_window, file_path)
    except Exception as e:
        print(e)


def open_file_dialog_and_open_file(main_window):
    # Open file dialog
    file_path, _ = QFileDialog.getOpenFileName(main_window, 'Open File')
    # Check if a file was selected
    if file_path:
        open_file_editor(main_window, file_path)
