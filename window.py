import markdown
import os
from PyQt5.QtWidgets import QWidget
from PyQt5.QtWebEngineWidgets import QWebEngineView
from PyQt5.QtCore import QTimer, QUrl


class AnotherWindow(QWidget):
    def __init__(self):
        filePath = os.path.realpath()
        self.view = QWebEngineView()
        self.timer = QTimer()
        super().__init__()
        self.view.load(QUrl.fromLocalFile(os.path.join(filePath,'test.html')))
        self.timer.timeout.connect(self.updateView())
        self.timer.start(1000)
    
    def updateView(self):
        self.writeMD()
        self.view.reload()
        self.view.show()
    
    def writeMD():
        with open(r"D:\Proyectos de Programación\python\Notepad\test.txt", "r", encoding="utf-8", newline='\n') as reader:
            text = reader.readlines()
            translator = markdown.markdown(text)

        with open(r"D:\Proyectos de Programación\python\Notepad\test.html", "w", encoding="utf-8", errors="xmlcharrefreplace",newline='') as outputFile:
            outputFile.writelines(translator)