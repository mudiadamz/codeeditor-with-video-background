import os


def generate_unique_name(path):
    base, extension = os.path.splitext(path)
    counter = 1
    new_path = f"{base} ({counter}){extension}"
    while os.path.exists(new_path):
        counter += 1
        new_path = f"{base} ({counter}){extension}"
    return new_path

