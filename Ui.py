from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import QtGui
from PyQt5 import uic

class MyGuI(QMainWindow):
    

    def __init__(self):
        super(MyGuI, self).__init__()
        uic.loadUi('editor.ui', self) #Nombre de la interfaz creada

        #Variables "Globales" para el uso de botones
        self.font = "Arial"
        self.size = 12
        self.weight = 300
        self.italic = False
        self.show()

        #Acciones de los botones
        self.setWindowTitle("Tendencias Desarrollo de Software - Notepad")

        #File
        self.actionOpen.triggered.connect(self.open_file)       #Abrir Archivo
        self.actionSave.triggered.connect(self.save_file)       #Guardar Archivo
        self.actionClose.triggered.connect(exit)                #Cerrar Archivo (Sin advertencias)

        #######

        #Edit
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)

        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)

        #######

        #Appearance
        self.action12pt.triggered.connect(lambda: self.change_size(12)) #Tamaño 12
        self.action18pt.triggered.connect(lambda: self.change_size(18)) #Tamaño 18
        self.action24pt.triggered.connect(lambda: self.change_size(24)) #Tamaño 24
        self.actionBold.triggered.connect(lambda: self.set_bold())      #Estilo Negrita
        self.actionItalic.triggered.connect(lambda: self.set_italic())  #Estilo Italica
        self.actionReset.triggered.connect(lambda: self.reset_style())  #Reiniciar estilo


    ##Metodos

    #File

    
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

    #######

    #Edit

    def undo(self):
        self.plainTextEdit.undo()

    def redo(self):
        self.plainTextEdit.redo()

    def cut(self):
        self.plainTextEdit.cut()

    def copy(self):
        self.plainTextEdit.copy()


    def paste(self):
        self.plainTextEdit.paste()

    #######

    #Appearance
    #Cambiar tamaño de letras
    def change_size(self, size):
        self.plainTextEdit.setFont(QFont(self.font, size,self.weight))
        self.size = size
    
    #Cambiar texto a negrita
    def set_bold(self):

        if self.weight != 500:
            self.weight = 500
            self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
        else:
            self.weight = 300
            self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
    
    #Cambiar texto a italico (?)
    def set_italic(self):
        
        if self.italic != True:
            self.italic = True
            self.plainTextEdit.setFont(QFont(self.font,self.size,self.weight,self.italic))
        else:
            self.italic = False
            self.plainTextEdit.setFont(QFont(self.font,self.size,self.weight,self.italic))

    #Remover el estilo de negrita (e / o) italico 
    def reset_style(self):
        self.plainTextEdit.setFont(QFont(self.font, self.size, 300, False))
        self.weight = 300
        self.italic = False