from pathlib import Path

from PySide6 import QtCore, QtWidgets


APP_NAME = "randomushroom"
APP_DISPLAY_NAME = "Randomushroom"
APP_ICON = "ico_randoglobin.ico"

QtWidgets.QApplication.setApplicationName(APP_NAME)
QtWidgets.QApplication.setApplicationDisplayName(APP_DISPLAY_NAME)


SCRIPT_DIR = Path(__file__).parent
FILES_DIR = SCRIPT_DIR / 'files'
LANG_DIR = SCRIPT_DIR / 'lang'