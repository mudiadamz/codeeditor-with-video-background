def detect_tab_size(file_path):
    tab_size = 0
    tab_type = "Space"

    if file_path is not None:
        with open(file_path, 'r') as f:
            lines = f.readlines()

        for line in lines:
            # Count leading whitespace characters (spaces and tabs)
            leading_spaces = len(line) - len(line.lstrip(' '))
            leading_tabs = len(line) - len(line.lstrip('\t'))

            if leading_spaces > 0:
                if tab_size == 0:
                    tab_size = leading_spaces
                elif leading_spaces % tab_size != 0:
                    tab_type = "Space"
                    break
            elif leading_tabs > 0:
                if tab_size == 0:
                    tab_size = leading_tabs
                elif leading_tabs != tab_size:
                    tab_type = "Tab"
                    break

    return tab_size, tab_type
