def ejercicioFibonacci(n):
  n = int(n)
  cadena = "El número en la posición "+str(n)+" de la sucesión es: "
  cadena += str(fibonacci(n))
  return cadena

def fibonacci(n):
  if n<=0:
    return "¡Pero introduce un número mayor que 0!"
  elif n==1:
    return 0
  elif n==2:
    return 1
  else:
    return fibonacci(n-1)+fibonacci(n-2)