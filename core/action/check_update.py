import requests
from PyQt6.QtCore import Qt, QRunnable, QThreadPool, pyqtSignal, QObject
from PyQt6.QtWidgets import QMessageBox, QProgressDialog

CURRENT_VERSION = "1.0.0"
UPDATE_URL = "https://xprimes.com"


class WorkerSignals(QObject):
    finished = pyqtSignal(object)


class CheckUpdateTask(QRunnable):
    def __init__(self, signals):
        super().__init__()
        self.signals = signals

    def run(self):
        try:
            response = requests.get(UPDATE_URL + "/editor/check_update")
            response.raise_for_status()
            data = response.json()
            self.signals.finished.emit(data)
        except requests.RequestException as e:
            self.signals.finished.emit(e)


def check_update(parent):
    progress = QProgressDialog("Checking for updates...", None, 0, 0, parent)
    progress.setWindowTitle("Update")
    progress.setWindowModality(Qt.WindowModality.ApplicationModal)
    progress.setCancelButton(None)
    progress.show()

    def on_finished(result):
        progress.close()
        if isinstance(result, Exception):
            QMessageBox.critical(parent, "Error", f"Failed to check for updates: {result}")
        else:
            latest_version = result.get("version")
            if latest_version and latest_version > CURRENT_VERSION:
                update_available(parent, latest_version)
            else:
                no_update_available(parent)

    signals = WorkerSignals()
    signals.finished.connect(on_finished)
    task = CheckUpdateTask(signals)
    QThreadPool.globalInstance().start(task)


def update_available(parent, latest_version):
    reply = QMessageBox.question(parent, "Update Available",
                                 f"Version {latest_version} is available. Do you want to update?",
                                 QMessageBox.StandardButton.Yes | QMessageBox.StandardButton.No)

    if reply == QMessageBox.StandardButton.Yes:
        perform_update(parent, latest_version)


def no_update_available(parent):
    QMessageBox.information(parent, "No Update Available", "You are already using the latest version.")


def perform_update(parent, latest_version):
    # Placeholder for OTA update logic
    try:
        download_url = f"{UPDATE_URL}/{latest_version}"
        download_path = "path/to/download/updated_executable.exe"

        response = requests.get(download_url)
        response.raise_for_status()

        with open(download_path, "wb") as f:
            f.write(response.content)

        # Implement the logic to replace the current executable with the downloaded one
        QMessageBox.information(parent, "Update Successful",
                                "The application has been updated. Please restart the application.")
    except requests.RequestException as e:
        QMessageBox.critical(parent, "Error", f"Failed to download the update: {e}")
