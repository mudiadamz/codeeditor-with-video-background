from PyQt6.QtWidgets import QMessageBox


def about_dialog(main_window):
    about_msg = QMessageBox(main_window)
    about_msg.setIcon(QMessageBox.Icon.Information)
    about_msg.setWindowTitle("About XPrimeEditor")
    about_msg.setText("XPrimeEditor\n\nVersion 1.0\n\n© 2024 www.xprimes.com")
    # about_msg.setStandardButtons(QMessageBox.StandardButton.Ok)
    about_msg.exec()
