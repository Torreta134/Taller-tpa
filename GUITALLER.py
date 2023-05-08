from PyQt6.QtWidgets import QApplication, QMainWindow, QWidget, QLabel, QHBoxLayout, QVBoxLayout, QPushButton, QLineEdit, QDialog
import sys

class Objeto:
    def __init__(self, nombre, atributo):
        self.nombre = nombre
        self.atributo = atributo

class VentanaPrincipal(QMainWindow):
    def __init__(self):
        super().__init__()
     # Crear los widgets principales
        self.texto_bienvenida = QLabel("¡Bienvenido!")
        self.texto_instrucciones = QLabel("Ingrese los datos de los objetos para compararlos.")
        self.panel_comparacion = QWidget()
        self.boton_actualizar = QPushButton("Comparar")

        # Crear los widgets para los objetos
        self.widget_objeto1 = QWidget()
        self.label_objeto1 = QLabel("Objeto 1")
        self.input_nombre_objeto1 = QLineEdit()
        self.input_atributo_objeto1 = QLineEdit()

        self.widget_objeto2 = QWidget()
        self.label_objeto2 = QLabel("Objeto 2")
        self.input_nombre_objeto2 = QLineEdit()
        self.input_atributo_objeto2 = QLineEdit()
        self.boton_ingresar = QPushButton("Ingresar")

        # Crear los layouts
        self.layout_principal = QVBoxLayout()
        self.layout_objetos = QHBoxLayout()
        self.layout_objeto1 = QVBoxLayout()
        self.layout_objeto2 = QVBoxLayout()

        # Añadir los widgets a los layouts correspondientes
        self.layout_objeto1.addWidget(self.label_objeto1)
        self.layout_objeto1.addWidget(self.input_nombre_objeto1)
        self.layout_objeto1.addWidget(self.input_atributo_objeto1)
        self.widget_objeto1.setLayout(self.layout_objeto1)

        self.layout_objeto2.addWidget(self.label_objeto2)
        self.layout_objeto2.addWidget(self.input_nombre_objeto2)
        self.layout_objeto2.addWidget(self.input_atributo_objeto2)
        self.widget_objeto2.setLayout(self.layout_objeto2)

        self.layout_objetos.addWidget(self.widget_objeto1)
        self.layout_objetos.addWidget(self.widget_objeto2)

        self.panel_comparacion.setLayout(self.layout_objetos)

        # Añadir los widgets a la ventana principal
        self.layout_principal.addWidget(self.texto_bienvenida)
        self.layout_principal.addWidget(self.texto_instrucciones)
        self.layout_principal.addWidget(self.panel_comparacion)
        self.layout_principal.addWidget(self.boton_actualizar)

        self.widget_principal = QWidget()
        self.widget_principal.setLayout(self.layout_principal)
        self.setCentralWidget(self.widget_principal)

        # Conectar el botón a la función de actualización
        self.boton_actualizar.clicked.connect(self.actualizar_comparacion)

    def actualizar_comparacion(self):
        # Obtener los datos ingresados
        nombre_objeto1 = self.input_nombre_objeto1.text()
        atributo_objeto1 = int(self.input_atributo_objeto1)





if __name__ == "__main__":
    app = QApplication(sys.argv)
    
    vista = VentanaPrincipal()
    vista.show()
    app.exec()

