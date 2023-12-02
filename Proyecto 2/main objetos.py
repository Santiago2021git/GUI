import sys
from PyQt5 import uic
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QFrame, QPushButton, QLabel, QStackedWidget

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        uic.loadUi("diseñointerfaz.ui", self)
        
        self.Submenu.hide()
        self.Ingreso_datos.hide()
        

        # Conectar señales a ranuras para mostrar y ocultar frames de submenu
        self.Cerrar.clicked.connect(self.cerrar_app)
        self.Salir.clicked.connect(self.salir_app)
        self.Maximo.clicked.connect(self.pantalla_maximizar)
        self.Minimo.clicked.connect(self.pantalla_minimizar)
        self.Minimizar.clicked.connect(self.minimizar_app)
        self.RegistroClientes.clicked.connect(self.mostrar_submenu_clientes)
        self.RegistroAntibioticos.clicked.connect(self.mostrar_submenu_antibioticos)
        self.RegistroPesticidas.clicked.connect(self.mostrar_submenu_pesticidas)
        self.RegistroFertilizantes.clicked.connect(self.mostrar_submenu_fertilizantes)
        self.Facturacion.clicked.connect(self.mostrar_submenu_factura)
        self.pushButton_5.clicked.connect(self.crear_antibiotico)
        self.pushButton_6.clicked.connect(self.listar_antibioticos)
        self.pushButton_7.clicked.connect(self.eliminar_antibioticos)
        self.pushButton_8.clicked.connect(self.cerrar_submenu)
        self.pushButton.clicked.connect(self.crear_cliente)
        self.pushButton_2.clicked.connect(self.listar_cliente)
        self.pushButton_3.clicked.connect(self.eliminar_cliente)
        self.pushButton_4.clicked.connect(self.cerrar_submenu)
        self.pushButton_17.clicked.connect(self.crear_factura)
        self.pushButton_19.clicked.connect(self.listar_factura)
        self.pushButton_21.clicked.connect(self.cerrar_submenu)
        self.pushButton_9.clicked.connect(self.crear_fertilizante)
        self.pushButton_10.clicked.connect(self.listar_fertilizante)
        self.pushButton_11.clicked.connect(self.eliminar_fertilizante)
        self.pushButton_12.clicked.connect(self.cerrar_submenu)
        self.pushButton_13.clicked.connect(self.crear_pesticida)
        self.pushButton_14.clicked.connect(self.listar_pesticida)
        self.pushButton_15.clicked.connect(self.eliminar_pesticida)
        self.pushButton_16.clicked.connect(self.cerrar_submenu)
        self.pushButton_23.clicked.connect(self.guardar_creacion_antibiotico)
        self.pushButton_28.clicked.connect(self.guardar_creacion_cliente)
        self.pushButton_22.clicked.connect(self.guardar_creacion_fertilizante)
        self.pushButton_24.clicked.connect(self.guardar_creacion_pesticida)
        #crear conexion para factura
        self.pushButton_25.clicked.connect(self.confirmar_eliminacion_antibiotico)
        self.pushButton_26.clicked.connect(self.confirmar_eliminacion_cliente)
        self.pushButton_27.clicked.connect(self.confirmar_eliminacion_fertilizante)
        self.pushButton_28.clicked.connect(self.confirmar_eliminacion_pesticida)
        """
        hacer conexion botones para listar si es que los hay
        """
        
    def mostrar_submenu_clientes (self) :
        self.Submenu.show()
        self.stackedWidget1Page1.show()
    
        
    def mostrar_submenu_antibioticos (self) :
        self.Submenu.show()
        self.stackedWidget1Page5.show()
        
    
    def mostrar_submenu_pesticidas (self) :
        self.Submenu.show()
        self.stackedWidget1Page2.show()
        
    def mostrar_submenu_fertilizantes (self) :
        self.Submenu.show()
        self.stackedWidget1Page3.show()
        
        
    def mostrar_submenu_factura (self) :
        self.Submenu.show()
        self.stackedWidget1Page4.show()

    def cerrar_submenu (self) :
        self.Submenu.hide()

    def crear_cliente (self) :
        self.Ingreso_datos.show()
        self.Crear_cliente.show()
        
        
    


    def confirmar_eliminacion_cliente () :
    
    def confirmar_eliminacion_fertilizante () :
    
    def confirmar_eliminacion_pesticida () :   
        
    def confirmar_eliminacion_antibiotico () :
        
        
    def guardar_creacion_antibiotico () :
        # crear metodo para almacenar datos
        
    def guardar_creacion_cliente () :
        
        
    def guardar_creacion_fertilizante () :
        
    def guardar_creacion_pesticida () :
        
    def guardar_creacion_factura () :
        
      
    def crear_pesticida () :
        stackedWidget_2.Crear_pesticida 
        
    def listar_pesticida () :
        stackedWidget_2.Listar_pesticida
        
    def eliminar_pesticida () :
        stackedWidget_2.Eliminar_pesticida
        
    def crear_fertilizante () :
        stackedWidget_2.Crear_pesticida
        
    def eliminar_fertilizante () : 
        stackedWidget_2.Eliminar_pesticida

    def listar_antibioticos () :
        stackedWidget_2.Listar_antibioticos
        
    def eliminar_antibioticos () :
        stackedWidget_2.Eliminar_antibioticos
        
    def cerrar_submenu (self) :
        self.Submenu.hide()
    def crear_cliente () :
        stackedWidget_2.Crear_cliente
    
    def listar_cliente () :
        stackedWidget_2.Listar_cliente
        
        
    def eliminar_cliente () :
        stackedWidget_2.Eliminar_cliente
        
    def crear_factura ():
        stackedWidget_2.Crear_factura
        
    def listar_factura () :
        stackedWidget_2.Listar_factura
           


        
    def cerrar_app(self):
        QApplication.quit()

    def salir_app(self):
        QApplication.quit()
        
        

if __name__ == "__main__":
    app = QApplication(sys.argv)
    GUI = MainWindow()
    GUI.show()
    sys.exit(app.exec_())

        
    
'''
from UI import InterfazGrafica

print("BIENVENIDO A LA TIENDA AGRICOLA S&S")

InterfazGrafica.escoger_opciones()
'''




      
