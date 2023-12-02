from UI import InterfazGrafica as IG
from CRUD import CRUD_cliente
from CRUD import CRUD_fertilizante
from CRUD import CRUD_antibiotico
from CRUD import CRUD_factura
from CRUD import CRUD_control_de_plagas


def retorno_interfaz():
    IG.escoger_opciones()


def llamar_interfaz_clientes():
    IG.print_options_cliente()


def retorno_encontrados_cliente(nombreb, cedulab, numero_de_facturasb):
    IG.impresion_encontrado(nombreb, cedulab, numero_de_facturasb)


def retorno_no_encontrados_cliente():
    IG.impresion_no_encontrados()


def crear_cliente(nombre, cedula):
    CRUD_cliente.crear_cliente(nombre, cedula)
    

def eliminar_cliente(cedula):
    CRUD_cliente.eliminar_cliente(cedula)


def buscar_cliente(cedula):
    CRUD_cliente.buscar_cliente(cedula)


def crear_factura(fecha):
    CRUD_factura.crear_factura(fecha)


def elegir_productos_factura():
    opcion = IG.elegir_productos_factura()
    return opcion


def agregar_factura(clientes):
    CRUD_factura.agregar_factura_a_cliente(clientes)


def llamdo_interfaz_factura():
    IG.print_options_factura()


def retorno_interfaz_antibiotico():
    IG.print_options_antibiotico()


def crear_antibiotico(nombre, dosis, precio):
    CRUD_antibiotico.crear_antibiotico(nombre, dosis, precio)


def eliminar_antibiotico(producto):
    CRUD_antibiotico.eliminar_antibiotico(producto)


def antibiotico_encontrado(nombreb, dosisb, tipo_animalb, preciob):
    IG.impresion_antibiotico_encontrado(nombreb, dosisb, tipo_animalb, preciob)


def antibiotico_no_encontrado():
    IG.impresion_antibiotico_no_encontrado()