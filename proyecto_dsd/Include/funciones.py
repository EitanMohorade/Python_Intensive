import datetime
'''
Una función que al pasarle una lista de números y
un número, nos devuelva cuantas veces se repite el valor.
La llamaremos contar_valor y recibirá dos parámetros: lista y numero.
'''
def contar_valor(lista, numero):
    contador = 0
    for item in lista:
        if item == numero:
            contador = contador + 1
    return contador
'''
Una función que al pasarle una lista de cadenas y una cadena
, nos devuelva cuantas veces se repite la cadena en la lista.

La llamaremos contar_cadena y recibirá dos parámetros: lista y cadena.
'''
def contar_cadena(lista, cadena):
    contador = 0
    for item in lista:
        if item == cadena:
            contador = contador + 1
    return contador
'''
También agregaremos una función calcular_edad
'''

def calcular_edad(fecha_nacimiento):
    fecha_nacimiento = datetime.datetime.strptime(fecha_nacimiento, "%d-%m-%Y")
    edad = datetime.datetime.now().year - fecha_nacimiento.year
    return edad