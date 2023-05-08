import sys

from PyQt6.QtCore import QSize, Qt
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QGridLayout, QPushButton, QStackedLayout, QVBoxLayout, QHBoxLayout, QWidget


# Importar modelo
from divisa import Divisa
divisa1 = []
# Una clase que define el diseño y comportamiento de una ventana (vista)
class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__() # permite inicializar los atributos y metodos de la clase QMainWindow
        
        # Sección del init para diseño...
        self.contador_clicks = 0
        self.setWindowTitle("Ingreso de datos")
        self.setFixedSize(QSize(600,300))
        caja_grande = QVBoxLayout()
        caja_superior = QHBoxLayout()
        self.caja_inferior = QStackedLayout()
        
      
        contenedor = QWidget()
        layout = QVBoxLayout(contenedor)
        

        texto_registrar = QLabel("INGRESO DE DATOS")
        formulario_registrar = QGridLayout()
        registrar_nDivisa = QLabel("Nombre divisa")
        self.registrar_entrada_nDivisa = QLineEdit()
        registrar_vDivisa = QLabel("Valor divisa")
        self.registrar_entrada_vDivisa = QLineEdit()
        registrar_vEquivalente = QLabel("Valor equivalente")
        self.registrar_entrada_vEquivalente = QLineEdit()
        
        registrar_btn = QPushButton("Guardar")
        registrar_btn.clicked.connect(self.registrar_modelo_divisa)
        
        formulario_registrar.addWidget(registrar_nDivisa, 0,0)
        formulario_registrar.addWidget(self.registrar_entrada_nDivisa, 0,1)
        formulario_registrar.addWidget(registrar_vDivisa, 2,0)
        formulario_registrar.addWidget(self.registrar_entrada_vDivisa, 2,1)
        formulario_registrar.addWidget(registrar_vEquivalente, 3,0)
        formulario_registrar.addWidget(self.registrar_entrada_vEquivalente, 3,1)
        formulario_registrar.addWidget(registrar_btn, 4,1)
        
        layout.addWidget(texto_registrar)
        layout.addLayout(formulario_registrar)
        
        
  
        self.caja_inferior.addWidget(contenedor)
    
        
        
        #Agregar los layout interiores al VBox
        caja_grande.addLayout(caja_superior)
        caja_grande.addLayout(self.caja_inferior)
        
        #asigna el layout a la ventana
        ventana = QWidget()
        ventana.setLayout(caja_grande)
        self.setCentralWidget(ventana)
        

        

    def registrar_modelo_divisa(self):
        global divisa1
        nDivisa = self.registrar_entrada_nDivisa.text()
        vDivisa = self.registrar_entrada_vDivisa.text()
        vEquivalente = self.registrar_entrada_vEquivalente.text()
        

        u = Divisa(nDivisa, vDivisa, vEquivalente)
        divisa1.append(u)
        

       
# Bloque principal del programa
if __name__ == "__main__":
    app = QApplication(sys.argv)
    ventana = VentanaPrincipal()
    ventana.show()
    app.exec()

