def balanceados(cadena):
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
        return "¡No están balanceados!"
  if len(stack) == 0: 
    return "¡Sí están balanceados!"
  else: 
    return "¡No están balanceados!"