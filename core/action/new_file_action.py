import os

from PyQt6.QtCore import QSortFilterProxyModel, Qt
from PyQt6.QtWidgets import QDialog

from core.util.uniqe_name_util import generate_unique_name
from core.widget.dialog_new_file import NewFileDialog


def add_file(main_window, file_tree_view, index):
    try:
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

        # Show the new file dialog
        dialog = NewFileDialog(main_window)
        if dialog.exec() == QDialog.DialogCode.Accepted:
            new_file_name = dialog.get_new_file_name()
            if new_file_name:
                new_file_path = os.path.join(target_directory_path, new_file_name)
                if os.path.exists(new_file_path):
                    new_file_path = generate_unique_name(new_file_path)
                # Create the new file
                with open(new_file_path, 'w') as f:
                    pass
                # Refresh the model to reflect the changes
                file_system_model.setData(source_index, new_file_name, Qt.ItemDataRole.EditRole)
                print(f"Successfully created file: {new_file_path}")

    except Exception as e:
        print(f"An error occurred: {e}")
