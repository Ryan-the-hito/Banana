app = QApplication(sys.argv)
app.setQuitOnLastWindowClosed(False)

# Create the icon
icon = QIcon("banana.icns")

# Create the tray
tray = QSystemTrayIcon()
tray.setIcon(icon)
tray.setVisible(True)

# Create the menu
menu = QMenu()

action3 = QAction("🍌 Show bananas!")
menu.addAction(action3)

action4 = QAction("🍴 Save this link in Safari!")
menu.addAction(action4)

action5 = QAction("🙆‍ Manually embed (AI)!")
menu.addAction(action5)

action6 = QAction("🤖 Chat with AI!")
action6.setCheckable(True)
menu.addAction(action6)

action8 = QAction("👀 Show delete button")
action8.setCheckable(True)
menu.addAction(action8)

menu.addSeparator()

action7 = QAction("⚙️ Settings")
menu.addAction(action7)

menu.addSeparator()

action2 = QAction("🆕 Check for Updates")
menu.addAction(action2)

action1 = QAction("ℹ️ About")
menu.addAction(action1)

menu.addSeparator()

# Add a Quit option to the menu.
quit = QAction("Quit")
quit.triggered.connect(app.quit)
menu.addAction(quit)

# Add the menu to the tray
tray.setContextMenu(menu)

# create a system menu
btna4 = QAction("&Show bananas!")
btna5 = QAction("&Save this link in Safari!")
sysmenu = QMenuBar()
file_menu = sysmenu.addMenu("&Actions")
file_menu.addAction(btna4)
file_menu.addAction(btna5)