from PyQt6.QtWidgets import QDialog, QVBoxLayout, QLabel, QLineEdit, QPushButton


class RenameDialog(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setWindowTitle("Rename")
        self.new_name_edit = QLineEdit()
        self.ok_button = QPushButton("OK")
        self.cancel_button = QPushButton("Cancel")

        layout = QVBoxLayout()
        layout.addWidget(QLabel("Enter new name:"))
        layout.addWidget(self.new_name_edit)
        layout.addWidget(self.ok_button)
        layout.addWidget(self.cancel_button)
        self.setLayout(layout)

        self.ok_button.clicked.connect(self.accept)  # Connect OK button to accept method
        self.cancel_button.clicked.connect(self.reject)

    def get_new_name(self):
        return self.new_name_edit.text()

    def accept(self):
        super().accept()  # Call the base accept method
        # Additional logic to be executed when OK is pressed
        # This is where you should trigger the renaming process
