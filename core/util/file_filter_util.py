from PyQt6.QtCore import QSortFilterProxyModel


class FileFilterProxyModel(QSortFilterProxyModel):
    def __init__(self, base_folder, *args, **kwargs):
        super().__init__(*args, **kwargs)
        # self.base_folder = parent_folder
        self.open_folder = base_folder

    def filterAcceptsRow(self, source_row, source_parent):
        model = self.sourceModel()
        index = model.index(source_row, 0, source_parent)
        if not index.isValid():
            return False

        loop_path = model.filePath(index)
        loop_path_slash = (loop_path + "/").replace("//", "/")
        open_folder_slash = (self.open_folder + "/").replace("//", "/")

        """ Exclude siblings folder """
        if open_folder_slash.count("/") == loop_path_slash.count("/") and open_folder_slash != loop_path_slash:
            return False

        """ Include ancestor """
        if self.open_folder.startswith(loop_path):
            return True

        """ Include the children """
        if loop_path.startswith(open_folder_slash):
            return True

        return False
