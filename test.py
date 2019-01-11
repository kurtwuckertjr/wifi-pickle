try:
    from PyQt4 import QtGui
    print("PyQt4 library OK.")
except ImportError as e:
    print("Import failed. PyQt4 library not found.")
    exit(1)

try:
    import core.utility.constants as C
    print("Wifi-Pickle core.utility.constants, C classes import OK.")
except ImportError as e:
    print("Import failed on core.utility.constants, C.")
    exit(1)

try:
    from core.loaders.checker.depedences import check_dep_pickle
    print("Wifi-Pickle core.loaders.checker.depedences, check_dep_pickle classes import OK.")
except ImportError as e:
    print("Import failed on core.loaders.checker.depedences, check_dep_pickle.")
    exit(1)

try:
    from core.utility.application import ApplicationLoop
    print("Wifi-Pickle ApplicationLoop classes import OK.")
except ImportError as e:
    print("Import failed on ApplicationLoop.")
    exit(1)

try:
    from core.loaders.checker.networkmanager import CLI_NetworkManager, UI_NetworkManager
    print("Wifi-Pickle core.loaders.checker.networkmanager, CLI_NetworkManager, UI_NetworkManager classes import OK.")
except ImportError as e:
    print("Import failed on core.loaders.checker.networkmanager, CLI_NetworkManager, UI_NetworkManager.")
    exit(1)

try:
    from core.main import Initialize
    print("Wifi-Pickle core.main, Initialize classes import OK.")
except ImportError as e:
    print("Import failed on core.main, Initialize.")
    exit(1)
