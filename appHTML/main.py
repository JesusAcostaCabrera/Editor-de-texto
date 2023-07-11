from PyQt5.QtWidgets import *
import md

def main():
    app = QApplication([])
    windows = md.MyGuI()
    app.exec_()


if __name__ == '__main__':
    main()