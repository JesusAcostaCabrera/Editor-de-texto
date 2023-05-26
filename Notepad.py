from PyQt5.QtWidgets import *
import Ui

def main():
    app = QApplication([])
    windows = Ui.MyGuI()
    app.exec_()


if __name__ == '__main__':
    main()