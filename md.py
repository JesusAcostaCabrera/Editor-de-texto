import os
import markdown
from PyQt5.QtWidgets import QWidget
from PyQt5.QtCore import QUrl
from PyQt5.QtWebEngineWidgets import QWebEngineView

class window(QWidget):
    def __init__(self):
        self.view = QWebEngineView()
        super().__init__()
        self.view.load(QUrl.fromLocalFile(r"D:\Proyectos de Programación\python\Notepad\test.html"))
        self.view.show()
