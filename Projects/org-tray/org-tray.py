from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
from PyQt5.QtCore import QUrl

def todo():
    QDesktopServices.openUrl(QUrl("org-protocol://capture?template=t"))

def bookmark():
    QDesktopServices.openUrl(QUrl("org-protocol://capture?template=b"))

app = QApplication([])
app.setQuitOnLastWindowClosed(False)

# Create the icon
# https://orgmode.org/img/org-mode-unicorn.png
icon = QIcon("org-mode-unicorn.png")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action1 = QAction("Todo")
action1.triggered.connect(todo)
menu.addAction(action1)

action2 = QAction("Bookmark")
action2.triggered.connect(bookmark)
menu.addAction(action2)

action3 = QAction("Quit")
action3.triggered.connect(app.quit)
menu.addAction(action3)

# Add the menu to the tray
tray.setContextMenu(menu)

app.exec_()
