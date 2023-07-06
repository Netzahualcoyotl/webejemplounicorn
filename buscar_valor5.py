# -*- coding: utf-8 -*-
# Importa la biblioteca pyexcel_ods
import ezodf
import os

nombre_archivo = ('/home/netza/Desktop/basededatos2/BD.ods')

def abrir_archivo(nombre_archivo):
    doc = ezodf.opendoc(nombre_archivo)
    hoja = doc.sheets['Hoja1']
    filas = []
    for row in range(hoja.nrows()):
        fila = []
        for col in range(hoja.ncols()):
            if hoja[row, col].value is None:
                fila.append("")
            else:
                fila.append(hoja[row, col].value)
        filas.append(fila)
    columnas = filas.pop(0)
    return columnas, filas

# Función que busca los valores en la hoja de cálculo
def buscar_valores(nombre, numero):
    # Busca los valores en la hoja de cálculo
    nombres_columnas, filas = abrir_archivo(nombre_archivo)
    valores = []
    for fila in filas:
        if fila[20] == nombre and fila[21] == numero:
            valores.append(fila)
    if not valores:
        return {'mensaje': 'No se encontraron resultados para la búsqueda.'}
    return {'nombres_columnas': nombres_columnas, 'valores': valores}

