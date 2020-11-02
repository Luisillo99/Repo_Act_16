# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox
from PySide2.QtCore import Slot
from ui_main_window import Ui_MainWindow
from Libreria.particula import Particula
from Libreria.organizador import Organizador

class MainWindow(QMainWindow):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.organizador = Organizador()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        self.ui.agregar_inicio_button.clicked.connect(self.agregar_ini)
        self.ui.agregar_final_button.clicked.connect(self.agregar_fin)
        self.ui.mostrar_button.clicked.connect(self.mostrar)
        self.ui.actionAbrir.triggered.connect(self.abrir_archivo)
        self.ui.actionGuardar.triggered.connect(self.guardar_archivo)
    @Slot()
    def abrir_archivo(self):
        ubicacion = QFileDialog.getOpenFileName(
            self,
            "Abrir",
            ".",
            "JSON (*.json)",
            )[0]
        if self.organizador.abrir(ubicacion):
            QMessageBox.information(
                self,
                "Operación Exitosa",
                "El archivo se abrió con éxito desde la direccion: \n" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error!",
                "El archivo no se logró abrir"
            ) 

    @Slot()
    def guardar_archivo(self):
        ubicacion = QFileDialog.getSaveFileName(self,
        'Guadar',
        '.',
        'JSON (*.json)')[0]
        if self.organizador.guardar(ubicacion):
            QMessageBox.information(
                self,
                "Operación Exitosa",
                "El archivo se guardó con éxito en la direccion: \n" + ubicacion
            )
        else:
            QMessageBox.critical(
                self,
                "Error!",
                "El archivo no se logró guardar"
            )
    
    @Slot()
    def agregar_ini(self):
        Id = self.ui.id.value()
        or_x = self.ui.origen_X.value()
        or_y = self.ui.origen_y.value()
        ds_x = self.ui.destino_x.value()
        ds_y = self.ui.destino_y.value()
        vel = self.ui.vel.value()
        red = self.ui.red.value()
        grn = self.ui.green.value()
        blu = self.ui.blue.value()
        part = Particula(Id,or_x,or_y,ds_x,ds_y,vel,red,grn,blu)
        self.organizador.agregar_inicio(part)
    @Slot()
    def agregar_fin(self):
        Id = self.ui.id.value()
        or_x = self.ui.origen_X.value()
        or_y = self.ui.origen_y.value()
        ds_x = self.ui.destino_x.value()
        ds_y = self.ui.destino_y.value()
        vel = self.ui.vel.value()
        red = self.ui.red.value()
        grn = self.ui.green.value()
        blu = self.ui.blue.value()
        part = Particula(Id,or_x,or_y,ds_x,ds_y,vel,red,grn,blu)
        self.organizador.agregar_final(part)

    def mostrar(self):
        self.ui.plainTextEdit.clear()
        self.ui.plainTextEdit.insertPlainText(str(self.organizador))
