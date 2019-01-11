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
