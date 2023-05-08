from PyQt6.QtWidgets import QApplication, QMainWindow, QLabel, QLineEdit, QPushButton, QVBoxLayout, QHBoxLayout, QWidget, QMessageBox
import sys

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()

        # Crear los widgets principales
        self.texto_bienvenida = QLabel("¡Bienvenido!")
        self.texto_instrucciones = QLabel("Ingrese los precios para comparar.")
        self.panel_comparacion = QWidget()
        self.boton_actualizar = QPushButton("Actualizar")

        # Crear los widgets para los precios
        self.widget_precio1 = QWidget()
        self.label_precio1 = QLabel("Precio 1:")
        self.input_precio1 = QLineEdit()
        self.input_precio1.setPlaceholderText("Ingrese el precio 1")

        self.widget_precio2 = QWidget()
        self.label_precio2 = QLabel("Precio 2:")
        self.input_precio2 = QLineEdit()
        self.input_precio2.setPlaceholderText("Ingrese el precio 2")

        # Crear los layouts
        self.layout_principal = QVBoxLayout()
        self.layout_precios = QHBoxLayout()
        self.layout_precio1 = QVBoxLayout()
        self.layout_precio2 = QVBoxLayout()

        # Añadir los widgets a los layouts correspondientes
        self.layout_precio1.addWidget(self.label_precio1)
        self.layout_precio1.addWidget(self.input_precio1)
        self.widget_precio1.setLayout(self.layout_precio1)

        self.layout_precio2.addWidget(self.label_precio2)
        self.layout_precio2.addWidget(self.input_precio2)
        self.widget_precio2.setLayout(self.layout_precio2)

        self.layout_precios.addWidget(self.widget_precio1)
        self.layout_precios.addWidget(self.widget_precio2)

        self.layout_principal.addWidget(self.texto_bienvenida)
        self.layout_principal.addWidget(self.texto_instrucciones)
        self.layout_principal.addLayout(self.layout_precios)
        self.layout_principal.addWidget(self.panel_comparacion)
        self.layout_principal.addWidget(self.boton_actualizar)

        # Establecer el layout principal
        widget_principal = QWidget()
        widget_principal.setLayout(self.layout_principal)
        self.setCentralWidget(widget_principal)

        # Conectar el botón de actualizar a la función de comparación
        self.boton_actualizar.clicked.connect(self.comparar_precios)

    def comparar_precios(self):
        try:
            precio1 = float(self.input_precio1.text())
            precio2 = float(self.input_precio2.text())

            mensaje = QMessageBox()

            if precio1 < precio2:
                mensaje.setText("El precio 1 es menor que el precio 2.")
            elif precio1 > precio2:
                mensaje.setText("El precio 1 es mayor que el precio 2.")
            else:
                mensaje.setText("Los precios son iguales.")

            mensaje.exec()
        except ValueError:
            mensaje_error = QMessageBox()
            mensaje_error.setText("Los precios ingresados no son válidos.")
            mensaje_error.exec()








if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    vista = VentanaPrincipal()
    vista.show()
    app.exec()

