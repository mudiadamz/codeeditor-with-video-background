import os

from PyQt6.QtCore import Qt, QSortFilterProxyModel
from PyQt6.QtWidgets import QDialog

from core.widget.dialog_rename_file import RenameDialog


def rename_item(main_window, file_tree_view, index):
    # Get the file name from the index using EditRole instead of DisplayRole
    file_name = index.data(Qt.ItemDataRole.EditRole)
    if file_name is None:  # Fallback in case EditRole is not available
        file_name = index.data(Qt.ItemDataRole.DisplayRole)

    # Create and show the rename dialog
    dialog = RenameDialog(main_window)
    dialog.new_name_edit.setText(file_name)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        new_name = dialog.get_new_name()

        # Get the file system model associated with the tree view

        # Get the model associated with the tree view
        model = file_tree_view.model()

        # Check if the model is a proxy model
        if isinstance(model, QSortFilterProxyModel):
            # If it's a proxy model, map the proxy index to the source model index
            source_index = model.mapToSource(index)
            # Get the source model
            file_system_model = model.sourceModel()
        else:
            # If it's not a proxy model, use the model directly
            source_index = index
            file_system_model = model

        # Get the absolute file path from the index
        old_file_path = file_system_model.filePath(source_index)

        # Construct the new file path
        new_file_path = os.path.join(os.path.dirname(old_file_path), new_name)

        try:
            # Rename the file/folder using os.rename
            os.rename(old_file_path, new_file_path)
            # Refresh the model to reflect the changes
            file_system_model.setData(source_index, new_name, Qt.ItemDataRole.EditRole)
            # Print a success message
            print(f"Successfully renamed {old_file_path} to {new_file_path}")
        except Exception as e:
            # Print the exception message if an error occurs
            print(f"An error occurred: {e}")
