'''import markdown
from PyQt5.QtWidgets import *
html = markdown.markdown("Hi")

def openFile():
        with open("Test.txt", "r", encoding="utf-8") as input_file:
            text = input_file.read()
        html = markdown.markdown(text)

        with open("test.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
            output_file.write(html)
            '''
import markdown
from PyQt5.QtCore import QTimer, QUrl
from PyQt5.QtWidgets import QMainWindow, QWidget, QVBoxLayout, QLabel
from PyQt5.QtWebEngineWidgets import QWebEngineView

import sys

class AnotherWindow(QWidget):
    def __init__(self):
        super().__init__()
        layout = QVBoxLayout()
        view = QWebEngineView()
        self.setWindowTitle("Vista MarkDown")

        # Cargar el archivo HTML
        file_path = r"D:\Proyectos de Programación\python\Notepad\Temp.html"
        view.load(QUrl.fromLocalFile(file_path))
        layout.addWidget(view)
        self.setLayout(layout)
    
    def Actualizar(self, texto):
        layout = QVBoxLayout()
        html = markdown.markdown(texto)

        view = QWebEngineView()
        view.load(html)
        layout.addWidget(view)

    # def __init__(self) -> None:
    #     def write_MD():
    #         with open("test.txt","r") as input_file:
    #             text = input_file.read()
    #             html = markdown.markdown(text)

    #         with open("test.html", "w") as output_file:
    #             output_file.write(html)
    #     app = QMainWindow()
    #     view = QWebEngineView()

    #     # Cargar el archivo HTML
    #     file_path = r"D:\Proyectos de Programación\python\Notepad\test.html"
    #     view.load(QUrl.fromLocalFile(file_path))

    #     def update_view():
    #         write_MD()
    #         view.reload()

    #     # Configurar el temporizador para actualizar cada 5 segundos
    #     timer = QTimer()
    #     timer.timeout.connect(update_view)
    #     timer.start(5000)
    #     view.show()
    #     app.exec()