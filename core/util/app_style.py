import os

from PyQt6.QtCore import QSettings
from PyQt6.QtWidgets import QApplication

from core.util.asset_path_util import asset_path


def apply_theme():
    settings = QSettings()
    theme = settings.value('theme', 'system')
    if theme == 'system':
        QApplication.instance().setStyleSheet('')
    elif theme == 'light':
        QApplication.instance().setStyleSheet('QMainWindow { background-color: white; color: black; }')
    elif theme == 'dark':
        QApplication.instance().setStyleSheet('QMainWindow { background-color: #2b2b2b; color: white; }')


def app_style(app):
    # set background
    current_dir = os.path.dirname(os.path.abspath(__file__))
    path_bg = asset_path("core/assets/bg.jpg")
    background_image_path = path_bg.replace('\\', '/')
    app.setStyleSheet(f"""
            /* Equivalent to BODY */
            QMainWindow {{
                background-image: url('{background_image_path}');
                background-position: center;
                background-repeat: no-repeat;
            }}
            /* I guess everything is widget, so it's equivalent to DIV */
            QWidget, QWidget::pane {{
                border: none;
                background-color: transparent;
            }}
            /* Top bar, tittle bar */
            #CustomTopBar{{
                background-color: rgba(10,10,10,0.90);
                backdrop-filter: blur(50px);
                margin-bottom: -20px;
            }}
            /*Menu and context menu*/
            QMenu {{
                background-color: rgba(0,0,0,0);
                color: white;
            }}
            QMenu::item {{
                padding: 5px 30px;
            }}
            QMenu::item:selected {{
                background-color: rgba(100,100,100,0.5);
            }}
            QMenu::item:pressed {{
                background-color: rgba(100,100,100,0.5);
            }}
            /* button */
            QDialog QPushButton, QMessageBox QPushButton {{
                background-color: rgba(25,25,25, 1);
                color: white;
                padding: 3px 5px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                cursor: pointer;
            }}
            /*short text edit*/
            QLineEdit{{
                background-color: rgba(45,45,45, 1);
                color: white;
                padding: 3px;
                text-align: center;
                text-decoration: none;
                display: inline-block;
                margin: 2px 0px;
                cursor: pointer;
            }}
            /* Main bar: file tree, editor */
            QSplitter{{
                background-color: rgba(10,10,10,0.85);
                backdrop-filter: blur(50px);
            }}
            /* TAB editor */
            QTabBar::tab {{
                background-color: rgba(30, 30, 30, 0.1);
            }}
            QTabBar::tab:hover, QTabBar::tab:selected{{
                background-color: rgba(100, 100, 100, 0.6);
            }}
            /* FILE TREE */
            QTreeView {{
                background-color: rgba(0,0,0,0.2);
                backdrop-filter: blur(50px);
                padding: 3px 5px;
            }}
            QTreeView::item:hover {{
                background-color: rgba(200,200,200,0.5);
            }}
            QTreeView::item:selected {{
                background-color: transparent;
                /*color: black;*/
            }}
            /* Other */
        """)
