def balanceados(cadena):
  pantalla = "<h1>¿Están los corchetes balanceados?</h1>"
  open_list = ["[","{","("] 
  close_list = ["]","}",")"] 
  stack = [] 
  for i in cadena: 
    if i in open_list: 
      stack.append(i) 
    elif i in close_list: 
      pos = close_list.index(i) 
      if ((len(stack) > 0) and
        (open_list[pos] == stack[len(stack)-1])): 
        stack.pop() 
      else: 
        return pantalla+"¡No lo están!"
  if len(stack) == 0: 
      return pantalla+"¡Sí lo están!"
  else: 
      return pantalla+"¡No lo están!"