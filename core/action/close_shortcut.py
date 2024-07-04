from core.action.tab_action import close_tab


def handle_close_shortcut(main_window):
    try:
        index = main_window.tab_widget.currentIndex()
        if index is not None:
            close_tab(main_window, index)
    except Exception as e:
        print(e)
