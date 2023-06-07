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
from PyQt5.QtWidgets import QApplication
from PyQt5.QtWebEngineWidgets import QWebEngineView
import sys

# Convertir el texto Markdown a HTML
def write_MD():
    with open("Test.txt", "r", encoding="utf-8") as input_file:
        text = input_file.read()
        html = markdown.markdown(text)

    with open("test.html", "w", encoding="utf-8", errors="xmlcharrefreplace") as output_file:
        output_file.write(html)
app = QApplication(sys.argv)
view = QWebEngineView()

# Cargar el archivo HTML
file_path = r"D:\Proyectos de Programación\python\Notepad\App Html\test.html"
view.load(QUrl.fromLocalFile(file_path))

def update_view():
    write_MD()
    view.reload()

# Configurar el temporizador para actualizar cada 5 segundos
timer = QTimer()
timer.timeout.connect(update_view)
timer.start(5000)
view.show()

sys.exit(app.exec_())