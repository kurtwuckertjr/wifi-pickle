try:
    from PyQt4 import QtGui
    from PyQt5 import QtWidgets, QtGui, QtCore
except ImportError as e:
    print("Import failed. PyQt4 or PyQt5 library not found.")
    exit(1)

try:
    import core.utility.constants as C
    from core.loaders.checker.depedences import check_dep_pickle
    from core.utility.application import ApplicationLoop
    from core.main import Initialize
    from core.loaders.checker.networkmanager import CLI_NetworkManager, UI_NetworkManager
    from core.utility.collection import SettingsINI
except ImportError as e:
    print("Import failed. One or more modules failed to import correctly.")
    exit(1)
