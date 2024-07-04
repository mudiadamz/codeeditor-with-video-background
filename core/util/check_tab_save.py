def is_tab_saved(main_window, index):
    if 0 <= index < len(main_window.file_paths):
        file_path = main_window.file_paths[index]
        if file_path:
            # Check if the content is the same as the content in the file_action.py
            content = main_window.tab_widget.widget(index).toPlainText()
            with open(file_path, 'r') as file:
                file_content = file.read()
            return content == file_content
    return True
