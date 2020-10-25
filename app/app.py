from flask import Flask, url_for
app = Flask(__name__)

import ejercicio2 as ej2
import ejercicio3 as ej3
import ejercicio4 as ej4
import ejercicio5 as ej5
import ejercicio6 as ej6
import opcional as op

@app.route('/')

def hello_world():
  return 'Hello, World!'

# Ejercicio 2
@app.route('/ordena/<lista>')
def ejercicio2(lista):
  return ej2.ordena(lista)

# Ejercicio 3
@app.route('/eratostenes/<int:n>')
def ejercicio3(n):
  return ej3.SieveOfEratosthenes(n)

# Ejercicio 4
@app.route('/fibonacci/<int:n>')
def ejercicio4(n):
  return ej4.ejercicioFibonacci(n)


# Ejercicio 5
@app.route('/ejercicio5/<cadena>')
def ejercicio5(cadena):
  return ej5.balanceados(cadena)


# Ejercicio 6
@app.route('/ejercicio6/<frase>')
def ejercicio6(frase):
  return ej6.reconocimiento(frase)

@app.errorhandler(404)
def noExistePagina(error):
  return "<h1>La página que intentas buscar no existe</h1>"

@app.route('/svg')
def opcional():
  return op.generarFigura()

with app.test_request_context():
  print(url_for('static', filename='index.html'))