import os

from PyQt6.QtCore import QSettings, QDir, QSortFilterProxyModel, QByteArray
from PyQt6.QtWidgets import QFileDialog

my_settings = QSettings("YourCompany", "YourApp")


def open_folder(main_window, file_system_model, file_tree_view):
    # Open file dialog to select a directory
    new_base_folder = QFileDialog.getExistingDirectory(main_window, 'Select Folder')
    parent_folder = os.path.dirname(new_base_folder)

    # Check if a folder was selected
    if new_base_folder:
        # Check if the model is a proxy model
        if isinstance(file_system_model, QSortFilterProxyModel):
            # If it's a proxy model, get the source model
            source_model = file_system_model.sourceModel()
            # Set the root path of the source model to the parent folder
            source_model.setRootPath(parent_folder)
            # Get the index for the new base folder in the source model
            source_index = source_model.index(new_base_folder)
            # Map the source index to the proxy model
            proxy_index = file_system_model.mapFromSource(source_index)

            # Update the tree view with the new root index
            file_tree_view.setRootIndex(proxy_index)
            file_tree_view.expand(proxy_index)
            file_tree_view.setCurrentIndex(proxy_index)
        else:
            # If it's not a proxy model, set the root path and update directly
            file_system_model.setRootPath(new_base_folder)
            folder_index = file_system_model.index(new_base_folder)

            file_tree_view.setRootIndex(folder_index)
            file_tree_view.expand(folder_index)
            file_tree_view.setCurrentIndex(folder_index)

        # Set value to setting
        my_settings.setValue("base_folder", new_base_folder)


def load_setting():
    base_folder = my_settings.value("base_folder", QDir.rootPath())
    window_geometry = my_settings.value("window_geometry", QByteArray())
    window_state = my_settings.value("window_state", QByteArray())
    open_tabs = my_settings.value("open_tabs", [])
    return base_folder, window_geometry, window_state, open_tabs


def save_setting(base_folder, window, open_tabs):
    my_settings.setValue("base_folder", base_folder)
    my_settings.setValue("window_geometry", window.saveGeometry())
    my_settings.setValue("window_state", window.saveState())
    my_settings.setValue("open_tabs", open_tabs)

