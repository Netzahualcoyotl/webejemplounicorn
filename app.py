# -*- coding: utf-8 -*-
# Importa las bibliotecas necesarias
from flask import Flask, render_template, request
from buscar_valor import buscar_valores
from static.estilos.estilo import establecer_estilos

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('formulario_busqueda.html')

@app.route('/buscar', methods=['POST'])
def procesar_busqueda():
    Estilos = establecer_estilos()
    # Obtiene el nombre y el número a buscar del formulario de búsqueda
    nombre = request.form['nombre']
    numero = request.form['numero']
    # Busca los valores en la hoja de cálculo
    resultado = buscar_valores(nombre, numero)    
    # Verifica si se encontraron resultados
    if 'mensaje' in resultado:
        return render_template('resultado.html', mensaje=resultado['mensaje'], estilos = Estilos['estilos4'])
    else:
        # Si se encontraron resultados, los muestra en la tabla de resultados
        nombres_columnas = resultado['nombres_columnas']
        valores = resultado['valores']
        return render_template('resultado.html', nombres_columnas=nombres_columnas, valores=valores, estilos = Estilos['estilos4'])

if __name__ == '__main__':
    app.run(debug=True)
  
  # Muestra los resultados en la página
 
