from core.widget.widget_sidebar_ctxmenu import SidebarContextMenu


def sidebar_ctx_action(main_window, file_tree_view, pos):
    # Get the index of the item at the clicked position
    index = file_tree_view.indexAt(pos)
    if index.isValid():
        menu = SidebarContextMenu(main_window, file_tree_view, index)
        """ Show the context menu at the clicked position """
        menu.exec(file_tree_view.viewport().mapToGlobal(pos))
