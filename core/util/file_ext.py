import os


def get_file_extension(file_path):
    if file_path is None:
        return None

    _, extension = os.path.splitext(file_path)
    return extension[1:].lower()  # Exclude the first character (dot) and convert to lowercase
