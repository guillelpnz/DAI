from flask import Flask, url_for, render_template, flash, redirect, request, session
app = Flask(__name__)

from pickleshare import PickleShareDB
import random
import time
import model

import ejercicio2 as ej2
import ejercicio3 as ej3
import ejercicio4 as ej4
import ejercicio5 as ej5
import ejercicio6 as ej6
import opcional as op


app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

# Numero ejercicio 1
num_random = random.randint(1,100)
i_ej1 = 0

# Paginas visitadas
paginas = []

@app.route('/')
def index():
  if "logged" in session.keys():
    paginas.append("index")
  return render_template('index.html', title='Arte', paginas=paginas)

# Login
@app.route('/login', methods=['GET', 'POST'])
def login():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("login")
  if request.method == 'POST':
    username = request.form['username']
    password = request.form['password']
    mensaje = model.login_BD(username, password)

    if mensaje == "Credenciales correctas":
      session['password'] = password
      return redirect(url_for('index'))
    else:
      return render_template('login.html', error=mensaje)
  else:
    return render_template('login.html', error=mensaje)

# Registro
@app.route('/register', methods=['GET', 'POST'])
def register():
    error = None
    if session['logged'] in session.keys():
      paginas.append("register")
    if request.method == 'POST':
      if request.form['password1'] != request.form['password2']:
        error = 'Las contraseñas no coinciden'
        return render_template('register.html', error=error)
      else:
        username = request.form['username']
        password = request.form['password1']
        if model.registrar_BD(username, password) == "Correcto":
          session['password'] = password
          return redirect(url_for('index'))
        else:
          error = "El usuario ya existe"
          return render_template('register.html', error=error)
    else:
      return render_template('register.html', error=error)

@app.route('/mis_datos', methods=['GET', 'POST'])
def misDatos():
  if "logged" in session.keys():
    paginas.append("mis_datos")
    model.misDatosBD(session['username'])
    return render_template('mis_datos.html')
  else:
    return "<h1>No tienes permisos para acceder a esta página</h1>"


@app.route('/editar_usuario', methods=['GET', 'POST'])
def editarUsuario():
  error = ""
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("editar_usuario")
    if request.method == 'POST':
      if request.form['password1'] != request.form['password2']:
        error = 'Las contraseñas no coinciden'
      else:
        username = request.form['username']
        password = request.form['password1']
        model.registrar_BD(username, password)
        session['password'] = password
        mensaje = "Contraseña cambiada con éxito"
    return render_template('editar_usuario.html', error=error, mensaje=mensaje)
  else:
    return "<h1>No tienes permisos para acceder a esta página</h1>"
# Pagina a la que un usuario no tiene permisos
@app.route('/error')
def sin_permiso():
  return "<h1>No tienes permiso para acceder a esta página</h1>"

# Desloguearse
@app.route('/unlog')
def unlog():
  if "logged" in session.keys():
    session.clear()
    paginas.clear()
    return redirect(url_for('index'))
    
  else:
    return "<h1>No tienes permiso para acceder a esta página</h1>"

# Ejercicio 1
@app.route('/ejercicio1',methods=['GET', 'POST'])
def ejercicio1():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("ejercicio1")
  if request.method == 'POST':
    numero = int(request.form['n'])
    global i_ej1
    i_ej1 = i_ej1 + 1

    if i_ej1 <= 10:
      if numero < 1 or numero > 100:
        i_ej1 = 0
        mensaje = "Error"
      elif numero == num_random:
        i_ej1 = 0
        mensaje = "¡Has acertado!"
      elif numero < num_random:
        mensaje = "El número es mayor"
      else:
        mensaje = "El número es menor"
    else:
      mensaje = "¡Has perdido! Has gastado tus 10 intentos"
      i_ej1 = 0
    
  return render_template('ejercicio1.html', mensaje=mensaje)

# Ejercicio 2
@app.route('/ejercicio2', methods=['GET', 'POST'])
def ejercicio2():
  mensaje1 = ""
  mensaje2 = ""
  if "logged" in session.keys():
    paginas.append("ejercicio2")

  if request.method == 'POST':
    lista_string = request.form['lista'].split()
    mapa = map(int, lista_string)
    lista_int = list(mapa)
    lista_int2 = lista_int

    ej2.bubbleSort(lista_int)
    ej2.selectionSort(lista_int2)

    mensaje1 = "Lista ordenada con el algoritmo burbuja: "+str(lista_int)
    mensaje2 = "Lista ordenada con el algoritmo de selección: "+str(lista_int2)

  return render_template('ejercicio2.html', mensaje1=mensaje1, mensaje2=mensaje2)

# Ejercicio 3
@app.route('/ejercicio3', methods=['GET', 'POST'])
def ejercicio3():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("ejercicio3")
  
  if request.method == 'POST':
    n = request.form['n']
    mensaje = ej3.SieveOfEratosthenes(n)
  
  return render_template('ejercicio3.html', mensaje=mensaje)

# Ejercicio 4
@app.route('/ejercicio4', methods=['GET', 'POST'])
def ejercicio4():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("ejercicio3")
  
  if request.method == 'POST':
    n = request.form['n']
    mensaje = ej4.ejercicioFibonacci(n)
  
  return render_template('ejercicio4.html', mensaje=mensaje)


# Ejercicio 5
@app.route('/ejercicio5', methods=['GET', 'POST'])
def ejercicio5():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("ejercicio5")
  
  if request.method == 'POST':
    cadena = request.form['cadena']
    mensaje = ej5.balanceados(cadena)
  
  return render_template('ejercicio5.html', mensaje=mensaje)

# Ejercicio 6
@app.route('/ejercicio6', methods=['GET', 'POST'])
def ejercicio6():
  mensaje = ""
  if "logged" in session.keys():
    paginas.append("ejercicio6")
  if request.method == 'POST':
    cadena = request.form['cadena']
    mensaje = ej6.reconocimiento(cadena)
  
  return render_template('ejercicio6.html', mensaje=mensaje)

@app.errorhandler(404)
def noExistePagina(error):
  return "<h1>La página que intentas buscar no existe</h1>"

@app.route('/svg')
def opcional():
  if "logged" in session.keys():
    paginas.append("svg")
  return op.generarFigura()

with app.test_request_context():
  print(url_for('static', filename='index.html'))