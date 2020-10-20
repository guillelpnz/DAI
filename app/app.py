from flask import Flask
app = Flask(__name__)

@app.route('/')

def hello_world():
  return 'Hello, World!'

#Ejercicio 2
@app.route('/ordena/<lista>')
def ordena(lista):
  return bubbleSort(lista)+selectionSort(lista)

def bubbleSort(lista):
  vector = lista.split(',')
  n = len(vector)

  for i in range(n-1):
    for j in range(0, n-i-1):
      if vector[j] > vector[j+1] :
        vector[j], vector[j+1] = vector[j+1], vector[j]
  
  cadena = "<h1>Ordenación por burbuja</h1>"
  cadena += "<h2>Vector inicial: "+lista+"</h2>"

  cadena = cadena + "<h2>Cadena final: "
  for i in range(0,n):
    cadena += vector[i]
    if i != n-1:
      cadena += ","

  cadena+="</h2>"
  return cadena

def selectionSort(lista):
  A = lista.split(',')
  for i in range(len(A)):
    min_idx = i
    for j in range(i+1, len(A)):
      if A[min_idx] > A[j]:
        min_idx = j
    A[i], A[min_idx] = A[min_idx], A[i]

  cadena = "<h1>Ordenación por selección</h1>"
  cadena += "<h2>Vector inicial: "+lista+"</h2>"

  cadena += "<h2>Cadena final: "
  for i in range(0,len(A)):
    cadena += A[i]
    if i != len(A)-1:
      cadena += ","

  cadena+="</h2>"
  return cadena

#Ejercicio 3
@app.route('/eratostenes/<int:n>')
def SieveOfEratosthenes(n): 
  prime = [True for i in range(n+1)] 
  p = 2
  while (p * p <= n): 
    if (prime[p] == True): 
      for i in range(p * p, n+1, p): 
        prime[i] = False
    p += 1
  cadena = "<h1>Números primos hasta "+str(n)+"</h1>"
  for p in range(0,n): 
    if prime[p]: 
      cadena += str(p)+", "

  cadena = cadena[:-2]
  return cadena