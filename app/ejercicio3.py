def SieveOfEratosthenes(n):
  cadena = ""
  n = int(n)
  prime = [True for i in range(n+1)] 
  p = 2
  while (p * p <= n): 
    if (prime[p] == True): 
      for i in range(p * p, n+1, p): 
        prime[i] = False
    p += 1

  for p in range(0,n):
    if prime[p]:
      cadena += str(p)+", "

  cadena = cadena[:-2]

  return cadena