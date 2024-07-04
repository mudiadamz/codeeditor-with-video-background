import os
import shutil

from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtWidgets import QMessageBox

from core.util.uniqe_name_util import generate_unique_name

copied_item_path = None
is_copied_directory = False


def copy_item(main_window, file_tree_view, index):
    global copied_item_path, is_copied_directory

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
    copied_item_path = file_system_model.filePath(source_index)

    # Determine if the item is a directory
    is_copied_directory = os.path.isdir(copied_item_path)

    # Print a success message
    print(f"Copied {copied_item_path}")


def paste_item(main_window, file_tree_view, index):
    global copied_item_path, is_copied_directory

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

    # Get the absolute file path of the target item
    target_item_path = file_system_model.filePath(source_index)

    # Determine the target directory path
    if os.path.isdir(target_item_path):
        target_directory_path = target_item_path
    else:
        target_directory_path = os.path.dirname(target_item_path)

    if copied_item_path is None:
        QMessageBox.warning(main_window, 'Paste Error', 'No item to paste.')
        return

    # Construct the target path
    target_path = os.path.join(target_directory_path, os.path.basename(copied_item_path))

    # If the target path already exists, generate a unique name
    if os.path.exists(target_path):
        target_path = generate_unique_name(target_path)

    try:
        if is_copied_directory:
            # Copy directory
            shutil.copytree(copied_item_path, target_path)
        else:
            # Copy file
            shutil.copy2(copied_item_path, target_path)

        # Print a success message
        print(f"Pasted {copied_item_path} to {target_path}")

        # Refresh the model to reflect the changes
        file_system_model.setData(source_index, os.path.basename(target_path), Qt.ItemDataRole.EditRole)

    except Exception as e:
        # Print the exception message if an error occurs
        print(f"An error occurred: {e}")
