# pylint: disable=missing-module-docstring
# pylint: disable=missing-class-docstring
# pylint: disable=missing-function-docstring
from PySide2.QtWidgets import QMainWindow, QFileDialog, QMessageBox, QTableWidgetItem
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
        self.ui.buscar_button.clicked.connect(self.buscar)
        self.ui.mostrar_tabla_button.clicked.connect(self.mostrar_tabla)
    
    @Slot()
    def buscar(self):
        key = int(self.ui.buscar_line_edit.text())
        find = False
        for particula in self.organizador:
            if key == particula.id:
                self.ui.tabla.setColumnCount(10)
                labels = ['ID','Origen en X','Origen en Y','Destino en X','Destino en Y','Velocidad','Distancia','Red','Green','Blue']
                self.ui.tabla.setHorizontalHeaderLabels(labels)
                self.ui.tabla.setRowCount(1)
                self.ui.tabla.setItem(0, 0, QTableWidgetItem(str(particula.id)))
                self.ui.tabla.setItem(0, 1, QTableWidgetItem(str(particula.or_x)))
                self.ui.tabla.setItem(0, 2, QTableWidgetItem(str(particula.or_y)))
                self.ui.tabla.setItem(0, 3, QTableWidgetItem(str(particula.de_x)))
                self.ui.tabla.setItem(0, 4, QTableWidgetItem(str(particula.de_y)))
                self.ui.tabla.setItem(0, 5, QTableWidgetItem(str(particula.vel)))
                self.ui.tabla.setItem(0, 6, QTableWidgetItem(str(particula.dis)))
                self.ui.tabla.setItem(0, 7, QTableWidgetItem(str(particula.red)))
                self.ui.tabla.setItem(0, 8, QTableWidgetItem(str(particula.green)))
                self.ui.tabla.setItem(0, 9, QTableWidgetItem(str(particula.blue)))
                find = True
                return
        if find == False:
            QMessageBox.warning(
                self,
                "Atención",
                f"La partícula '{key}' no fue encontrada"
            )

    @Slot()
    def mostrar_tabla(self):
        self.ui.tabla.setColumnCount(10)
        labels = ['ID','Origen en X','Origen en Y','Destino en X','Destino en Y','Velocidad','Distancia','Red','Green','Blue']
        self.ui.tabla.setHorizontalHeaderLabels(labels)
        self.ui.tabla.setRowCount(len(self.organizador))
        
        fila=0
        for particula in self.organizador:
            self.ui.tabla.setItem(fila, 0, QTableWidgetItem(str(particula.id)))
            self.ui.tabla.setItem(fila, 1, QTableWidgetItem(str(particula.or_x)))
            self.ui.tabla.setItem(fila, 2, QTableWidgetItem(str(particula.or_y)))
            self.ui.tabla.setItem(fila, 3, QTableWidgetItem(str(particula.de_x)))
            self.ui.tabla.setItem(fila, 4, QTableWidgetItem(str(particula.de_y)))
            self.ui.tabla.setItem(fila, 5, QTableWidgetItem(str(particula.vel)))
            self.ui.tabla.setItem(fila, 6, QTableWidgetItem(str(particula.dis)))
            self.ui.tabla.setItem(fila, 7, QTableWidgetItem(str(particula.red)))
            self.ui.tabla.setItem(fila, 8, QTableWidgetItem(str(particula.green)))
            self.ui.tabla.setItem(fila, 9, QTableWidgetItem(str(particula.blue)))
            fila += 1

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
