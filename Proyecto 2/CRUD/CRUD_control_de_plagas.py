from MODELO import Plagas
from UI import InterfazGrafica


registros_pesticidas = []


def crear_pesticida():
    (registro_ica, nombre_del_producto, frecuencia_de_aplicacion, valor_del_producto,
     periodo_de_carencia) = InterfazGrafica.ingreso_de_datos_fertilizante()
    mi_fertilizante = Plagas.Plaga(registro_ica, nombre_del_producto, frecuencia_de_aplicacion,
                                   valor_del_producto, periodo_de_carencia)
    registros_pesticidas.append(mi_fertilizante)
    InterfazGrafica.print_options_plagas()


def eliminar_pesticida():
    producto = InterfazGrafica.ingreso_datos_eliminar_plaga()
    producto = producto.upper()
    tamaño = len(registros_pesticidas)
    eliminador = 0
    while eliminador <= tamaño - 1:
        eliminar = registros_pesticidas[eliminador]._nombre_del_producto.upper()
        if producto == eliminar:
            del registros_pesticidas[eliminador]
            break

        eliminador += 1
    InterfazGrafica.print_options_plagas()


def buscar_producto():
    producto = InterfazGrafica.ingreso_datos_busqueda_plaga()
    producto = producto.upper()
    tamaño = len(registros_pesticidas)
    buscador = 0
    while buscador <= tamaño - 1:
        buscar = registros_pesticidas[buscador]._nombre_del_producto.upper()
        if producto == buscar:
            Registrob = registros_pesticidas[buscador]._registro_ica
            Nombreb = registros_pesticidas[buscador]._nombre_del_producto
            Frecuenciab = registros_pesticidas[buscador]._frecuencia_de_aplicacion
            Preciob = registros_pesticidas[buscador]._valor_del_producto
            Periodob = registros_pesticidas[buscador]._periodo_de_carencia
            InterfazGrafica.impresion_plaga_encontrado(Registrob, Nombreb, Frecuenciab, Preciob, Periodob)
            break

        buscador += 1

    if buscador == tamaño:
        InterfazGrafica.impresion_plaga_no_encontrado()
    
    InterfazGrafica.escoger_opciones()
    return registros_pesticidas[buscador]

