import os
import shutil

from PyQt6.QtCore import QSortFilterProxyModel
from PyQt6.QtWidgets import QMessageBox


def delete_item(main_window, file_tree_view, index):
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
    file_path = file_system_model.filePath(source_index)

    # Confirm deletion with the user
    reply = QMessageBox.question(main_window, 'Confirm Delete',
                                 f"Are you sure you want to delete '{file_path}'?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No,
                                 QMessageBox.StandardButton.No)

    if reply == QMessageBox.StandardButton.Yes:
        try:
            if os.path.isdir(file_path):
                # Remove directory
                shutil.rmtree(file_path)
            else:
                # Remove file
                os.remove(file_path)

            # Remove the item from the model
            file_system_model.remove(source_index)

            # Print a success message
            print(f"Successfully deleted {file_path}")
        except Exception as e:
            # Print the exception message if an error occurs
            print(f"An error occurred: {e}")

