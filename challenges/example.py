operacionesPreDefinidas = ("+", "-", "*")

def calculadora(cantNum, operacion):
    contador = 0
    listaNum = []
    
    while contador < cantNum:
        numero = int(input(f"ingresar numero {contador}: "))
        listaNum.append(numero)
        contador += 1
        
    contador = 0
    
    while contador < listaNum.count(): #esto ya no sirve ya q deberia ir un if
        print(listaNum[contador] + operacion)
        contador += 1
        
    return listaNum

numeros = calculadora(2, operacionesPreDefinidas[0])
