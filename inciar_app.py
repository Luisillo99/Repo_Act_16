# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
import sys
from PySide2.QtWidgets import QApplication
from main_window import MainWindow

# Aplicación de Qt
app = QApplication()

window = MainWindow()

window.show()

sys.exit(app.exec_())
