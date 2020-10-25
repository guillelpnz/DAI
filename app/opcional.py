import random

def generarFigura():

    cadena = "<h1>Imágenes vectoriales</h1> "
    cuadradoAzul="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
    width="120" height="100" viewBox="0 0 120 100">
    <rect x="10" y="10" width="100" height="80"
    fill="RoyalBlue" /></svg>"""

    cuadradoRojo="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
    width="120" height="100" viewBox="0 0 120 100">
    <rect x="30" y="10" width="120" height="80"
    fill="Red" /></svg>"""

    circuloAzul="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
    width="120" height="120" viewBox="0 0 120 120">
    <circle cx="120" cy="60" r="50"
    fill="RoyalBlue" />
    </svg>"""

    circuloRojo="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
    width="120" height="120" viewBox="0 0 120 120">
    <circle cx="120" cy="60" r="50"
    fill="Red" />
    </svg>"""

    elipseAzul="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
    width="140" height="80" viewBox="0 0 140 80">
    <ellipse cx="30" cy="50" rx="60" ry="30"
    fill="RoyalBlue" />
    </svg>"""

    elipseRoja="""<svg version="1.1" xmlns="http://www.w3.org/2000/svg"
     width="37" height="100" viewBox="0 0 140 80">
    <ellipse cx="70" cy="40" rx="60" ry="30"
    fill="Red" />
    </svg>"""

    lista = [cuadradoAzul, cuadradoRojo, circuloAzul, circuloRojo, elipseAzul, elipseRoja]

    return cadena+random.choice(lista)
