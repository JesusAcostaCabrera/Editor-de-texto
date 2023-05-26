from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5 import uic

font = "Arial"

class MyGuI(QMainWindow):
    

    def __init__(self):
        super(MyGuI, self).__init__()
        uic.loadUi('editor.ui', self)
        self.size = 0
        self.show()

        self.setWindowTitle("Tendencias Desarrollo de Software - Notepad")
        self.action12pt.triggered.connect(lambda: self.change_size(12))
        self.action18pt.triggered.connect(lambda: self.change_size(18))
        self.action24pt.triggered.connect(lambda: self.change_size(24))
        self.actionBold.triggered.connect(lambda: self.set_bold())

        self.actionOpen.triggered.connect(self.open_file)
        self.actionSave.triggered.connect(self.save_file)
        self.actionClose.triggered.connect(exit)

    #Cambiar tamaño de letras
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont(font, size))
        self.size = size
    
    #Abrir Archivo
    def open_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getOpenFileName(self, "OpenFile","", "TextFiles (*.txt);;Python Files (*.py)", options=options)
        if filename != "":
            with open(filename, "r") as f:
                self.plainTextEdit.setPlainText(f.read())

    #Guardar Archivo
    def save_file(self):
        options = QFileDialog.Options()
        filename, _ = QFileDialog.getSaveFileName(self, "Save", "", "Text Files (*.txt);;All Files (*)", options=options)
        if filename != "":
            with open(filename, "w") as f:
                f.write(self.plainTextEdit.toPlainText())
    
    #Cerrar con X
    def closeEvent(self, event):
        dialog = QMessageBox()
        if self.plainTextEdit.toPlainText() != "":
            dialog.setText("Do you want to save your work?")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole) #0
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole) #1
            dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) #2
            answer = dialog.exec_()
            if answer == 0:
                self.save_file()
                event.accept()
            elif answer == 2:
                event.ignore()