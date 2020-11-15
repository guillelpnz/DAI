import random

def adivina(numero, num_random):
    num_random = random.randint(1,100)
    i=0
    while numero < 1 or numero > 100 or numero != random or i<10 :
        if numero < random:
            return "Mayor"
        elif numero > random:
            return "Menor"
        else:
            break
        i = i + 1

    if i == 10:
        return "Has gastado todos tus intentos")
    else:
        return "Correcto"