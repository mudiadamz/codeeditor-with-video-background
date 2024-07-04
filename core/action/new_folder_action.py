import os

from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtWidgets import QDialog

from core.util.uniqe_name_util import generate_unique_name
from core.widget.dialog_new_folder import NewFolderDialog


def add_folder(main_window, file_tree_view, index):
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

    # Determine the target directory path
    target_item_path = file_system_model.filePath(source_index)
    if os.path.isdir(target_item_path):
        target_directory_path = target_item_path
    else:
        target_directory_path = os.path.dirname(target_item_path)

    # Show the new folder dialog
    dialog = NewFolderDialog(main_window)
    if dialog.exec() == QDialog.DialogCode.Accepted:
        new_folder_name = dialog.get_new_folder_name()
        if new_folder_name:
            new_folder_path = os.path.join(target_directory_path, new_folder_name)
            if os.path.exists(new_folder_path):
                new_folder_path = generate_unique_name(new_folder_path)
            try:
                # Create the new folder
                os.makedirs(new_folder_path)
                # Refresh the model to reflect the changes
                file_system_model.setData(source_index, new_folder_name, Qt.ItemDataRole.EditRole)
                print(f"Successfully created folder: {new_folder_path}")
            except Exception as e:
                print(f"An error occurred: {e}")
