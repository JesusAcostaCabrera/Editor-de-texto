"""
Inicio de la app
"""
from PyQt5.QtWidgets import QApplication
import Ui

def main():
    app = QApplication([])
    windows = Ui.uiMainWindow()
    app.exec_()


if __name__ == '__main__':
    main()
