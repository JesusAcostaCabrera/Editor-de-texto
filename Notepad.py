"""
Inicio de la app
"""
from PyQt5.QtWidgets import QApplication
import Ui
import sys


def main():
    app = QApplication([])  
    windows = Ui.uiMainWindow()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()