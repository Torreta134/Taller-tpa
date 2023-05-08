
from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox, QDialog, QGridLayout
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()


        # Crear los widgets principales
        self.texto_bienvenida = QLabel("¡Bienvenido!")
        self.texto_instrucciones = QLabel("Ingrese los precios para comparar.")
        self.panel_comparacion = QWidget()
        self.boton_ingresar_precio = QPushButton("Ingresar precio")
        self.boton_comparar_precios = QPushButton("Comparar precios")
        #boton2
        self.boton_ingresar_precio1 = QPushButton("Ingresar precio")
        self.boton_comparar_precios1 = QPushButton("Comparar precios")
        self.precios = []

        # Crear los widgets para los precios
        self.widget_precios = QWidget()
        self.layout_precios = QVBoxLayout()

        # Añadir los widgets a los layouts correspondientes
        self.layout_principal = QVBoxLayout()
        self.layout_principal.addWidget(self.texto_bienvenida)
        self.layout_principal.addWidget(self.texto_instrucciones)
        self.layout_principal.addWidget(self.boton_ingresar_precio)
        self.layout_principal.addWidget(self.boton_ingresar_precio1)
        self.layout_principal.addWidget(self.widget_precios)
        self.layout_principal.addWidget(self.panel_comparacion)
        self.layout_principal.addWidget(self.boton_comparar_precios)

        # Establecer el layout principal
        widget_principal = QWidget()
        widget_principal.setLayout(self.layout_principal)
        self.setCentralWidget(widget_principal)

        # Conectar los botones a las funciones correspondientes
        self.boton_ingresar_precio.clicked.connect(self.ingresar_precio)
        self.boton_comparar_precios.clicked.connect(self.comparar_precios)
        self.boton_ingresar_precio1.clicked.connect(self.ingresar_precio)

    def ingresar_precio(self):
        ventana_ingreso = VentanaIngreso(self)
        ventana_ingreso.exec()

    def agregar_precio(self, precio):
        self.precios.append(precio)
        self.layout_precios.addWidget(QLabel(str(precio)))
        self.widget_precios.setLayout(self.layout_precios)

    def comparar_precios(self):
        if len(self.precios) < 2:
            mensaje_error = QMessageBox()
            mensaje_error.setText("Ingrese al menos dos precios para comparar.")
            mensaje_error.exec()
        else:
            precios_ordenados = sorted(self.precios)
            mensaje = QMessageBox()
            mensaje.setText(f"{precios_ordenados[0]}, < {precios_ordenados[-1]}.")
            mensaje.exec()

class VentanaIngreso(QDialog):
    def __init__(self, parent=None):
        super().__init__(parent)

        # Crear los widgets principales
        self.texto_instrucciones = QLabel("Ingrese el precio:")
        self.input_precio = QLineEdit()
        self.boton_ingresar = QPushButton("Ingresar")

        # Crear el layout y añadir los widgets
        self.layout = QGridLayout()
        self.layout.addWidget(self.texto_instrucciones, 0, 0)
        self.layout.addWidget(self.input_precio, 0, 1)
        self.layout

        self.layout.addWidget(self.boton_ingresar, 1, 1)

        # Establecer el layout
        self.setLayout(self.layout)

        # Conectar el botón a la función de ingreso
        self.boton_ingresar.clicked.connect(self.ingresar_precio)

    def ingresar_precio(self):
        precio = self.input_precio.text()
        if precio:
            try:
                precio = float(precio)
            except ValueError:
                mensaje_error = QMessageBox()
                mensaje_error.setText("Ingrese un valor numérico válido.")
                mensaje_error.exec()
                return
            self.parent().agregar_precio(precio)
            self.close()
        else:
            mensaje_error = QMessageBox()
            mensaje_error.setText("Ingrese un precio.")
            mensaje_error.exec()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    vista = VentanaPrincipal()
    vista.show()
    app.exec()




if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    vista = VentanaPrincipal()
    vista.show()
    app.exec()