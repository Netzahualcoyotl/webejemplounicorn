import ezodf

nombre_archivo = '/home/netza/Desktop/webejemplo/BD.ods'

def abrir_archivo(nombre_archivo):
    doc = ezodf.opendoc(nombre_archivo)
    hoja = doc.sheets['Hoja1']
    filas = []
    for row in hoja.rows():
        fila = []
        for cell in row:
            if cell.value is None:
                fila.append("")
            else:
                fila.append(cell.value)
        filas.append(fila)
    columnas = filas.pop(0)
    return columnas, filas

def buscar_valores(nombre, numero):
    columnas, filas = abrir_archivo(nombre_archivo)
    resultados = []
    resultados.append(columnas)    
    for fila in filas[1:]: # saltar la fila de encabezado
        if fila[18] == nombre:
            try:
                if int(fila[19]) == int(numero):
                    resultados.append(fila)
            except ValueError:
                 if fila[21] == numero:
                    resultados.append(fila)
    
    if not resultados:
        return {'mensaje': 'No se encontraron resultados para la búsqueda.'}
    #return {'resultados': resultados}
    return {'nombres_columnas': columnas, 'valores': resultados}

