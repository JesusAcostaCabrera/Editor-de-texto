from PyQt5.QtWidgets import *
from PyQt5.QtGui import QFont
from PyQt5 import uic
from PyQt5.QtCore import QTimer
from dotenv import load_dotenv
from pathlib import Path
import time
import os
import appHTML.md as md
import markdown

class uiMainWindow(QMainWindow):
       
    def __init__(self):
        load_dotenv()
        super(uiMainWindow, self).__init__()
        uic.loadUi('editor.ui', self) #Nombre de la interfaz creada
        

        #Variables "Globales" para el uso de botones
        dotenv_path = Path('Notepad\.env')
        self.w = md.AnotherWindow()  # No external window yet.
        self.active = False
        self.Path = ""
        self.font = os.getenv("FONT")
        self.size = int(os.getenv("SIZE"))
        self.weight = int(os.getenv("WEIGHT"))
        self.italic = bool(os.getenv("ITALIC"))
        self.wrap = bool(os.getenv("WRAP"))
        self.show()

        #Acciones de los botones
        self.setWindowTitle(os.getenv("TITLE"))

        #File
        self.actionNew.triggered.connect(self.newFile)
        self.actionOpen.triggered.connect(self.openFile)       #Abrir Archivo
        self.actionSave.triggered.connect(self.saveFile)       #Guardar Archivo

        #######

        #Edit
        self.actionUndo.triggered.connect(self.undo)
        self.actionRedo.triggered.connect(self.redo)

        self.actionCut.triggered.connect(self.cut)
        self.actionCopy.triggered.connect(self.copy)
        self.actionPaste.triggered.connect(self.paste)
        self.actionWrap.triggered.connect(self.wordWrap)

        #######

        #Appearance
        self.actionIncrease.triggered.connect(self.IncreaseFont) #Incrementar tamaño
        self.actionDecrease.triggered.connect(self.DecreaseFont) #Disminuir tamaño
        self.actionArial.triggered.connect(lambda: self.ChangeFont("Arial")) #Letra arial
        self.actionTimes.triggered.connect(lambda: self.ChangeFont("Times New Roman")) #Letra times new roman
        self.actionBold.triggered.connect(self.setBold)         #Estilo Negrita
        self.actionItalic.triggered.connect(self.setItalic)     #Estilo Italica
        self.actionReset.triggered.connect(self.resetStyle)     #Reiniciar estilo
        self.actionDark.triggered.connect(self.setDarkMode)     #Modo Luz
        self.actionLight.triggered.connect(self.setLightMode)   #Modo Oscuridad

        #MarkDown
        self.actionMD.clicked.connect(self.show_new_window)
        self.actionUpdateMD.triggered.connect(self.load_md)
    ##Metodos
    def moveEvent(self, event):
        super(uiMainWindow, self).moveEvent(event)
        diff = event.pos() - event.oldPos()
        geo = self.w.geometry()
        geo.moveTopLeft(geo.topLeft() + diff)
        self.w.setGeometry(geo)

    #File
    def show_new_window(self):
        geo = self.geometry()
        geo.moveLeft(geo.left() + geo.width() + 5)
        self.w.setGeometry(geo)
        if self.active == False or self.w == None:
            self.w.show()
            self.active = True
        else:
            self.w = None  # Discard reference, close window.
            self.w = md.AnotherWindow()
            self.active = False

    def load_md(self):
        with open("Temp.html", "w") as output_file:
            output_file.write(markdown.markdown(self.plainTextEdit.toPlainText()))
        
        if self.w != None:
            self.w = None
            self.w = md.AnotherWindow()
            self.active = False
            self.show_new_window()
    def clear_md(self):
        with open("Temp.html", "w") as output_file:
            output_file.write("")
            
    def newFile(self):
        cancel = False
        dialog = QMessageBox()
        if self.plainTextEdit.toPlainText() != "":
            dialog.setText("Do you want to save your work?")
            dialog.addButton(QPushButton("Yes"), QMessageBox.YesRole) #0
            dialog.addButton(QPushButton("No"), QMessageBox.NoRole) #1
            dialog.addButton(QPushButton("Cancel"), QMessageBox.RejectRole) #2
            answer = dialog.exec_()
            if answer == 0:
                self.saveFile()
            if answer == 2:
                cancel = True
            self.Path = ""
        if cancel == False:
            self.plainTextEdit.clear()
            self.resetStyle()
            self.setWindowTitle("Untitled")

        self.load_md()

    #Abrir Archivo
    def openFile(self):
        options = QFileDialog.Options()
        self.Path, _ = QFileDialog.getOpenFileName(self, "OpenFile","", "TextFiles (*.txt);;Python Files (*.py);;All Files (*)", options=options)
        if self.Path != "":
            self.setWindowTitle(self.Path)
            with open(self.Path, "r") as f:
                self.plainTextEdit.setPlainText(f.read())
        
        self.load_md()

    #Guardar Archivo
    def saveFile(self):
        if self.Path == "":
            options = QFileDialog.Options()
            self.Path, _ = QFileDialog.getSaveFileName(self, "Save", "", "Text Files (*.txt);;All Files (*)", options=options)
            if self.Path != "":
                with open(self.Path, "w") as f:
                    f.write(self.plainTextEdit.toPlainText())
        else:
            with open(self.Path, "w") as f:
                    f.write(self.plainTextEdit.toPlainText())
        
        self.load_md()
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
                self.saveFile()
                event.accept()
            elif answer == 2:
                event.ignore()
        
        with open("Temp.html", "w") as output_file:
            output_file.write("")
        
        self.w.close()
        

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
    
    def wordWrap(self):
        
        if self.wrap == True:
            self.plainTextEdit.setWordWrapMode(False)
            self.wrap = False
        else:
            self.plainTextEdit.setWordWrapMode(True)
            self.wrap = True

    #######

    #Appearance
    #Cambiar tamaño de letras
    def IncreaseFont(self):
        self.size += 1
        self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))

    def DecreaseFont(self):
        self.size -= 1
        self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
    
    #Cambiar tripos de letras

    def ChangeFont(self, font):
        self.font = font
        self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
    
    #Cambiar texto a negrita
    def setBold(self):

        if self.weight != 500:
            self.weight = 500
            self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
        else:
            self.weight = 300
            self.plainTextEdit.setFont(QFont(self.font, self.size, self.weight, self.italic))
    
    #Cambiar texto a italico (?)
    def setItalic(self):
        
        if self.italic != True:
            self.italic = True
            self.plainTextEdit.setFont(QFont(self.font,self.size,self.weight,self.italic))
        else:
            self.italic = False
            self.plainTextEdit.setFont(QFont(self.font,self.size,self.weight,self.italic))

    #Remover el estilo de negrita (e / o) italico 
    def resetStyle(self):
        self.plainTextEdit.setFont(QFont(self.font, self.size, 300, False))
        self.weight = 300
        self.italic = False

    def setDarkMode(self):
        self.setStyleSheet('''QWidget{
                                    background-color : rgb(33,33,33);
                                    color: #FFFFFF
                                    }

                                    QPlainTextEdit{
                                    background-color : rgb(46,46,46)
                                    }

                                    QMenuBar::item:selected{
                                    color: #000000
                                    }

                                    QMenu::item:selected{
                                    background-color : rgb(46,46,46)
                                    }
                            ''')

    def setLightMode(self):
        self.setStyleSheet("")

    def Check(self, event):
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