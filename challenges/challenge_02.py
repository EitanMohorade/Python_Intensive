''' PUNTO UNO
Operadores lógicos: Escribí un código que determine 
si un número ingresado por el usuario es par y 
divisible por 7. Usa los operadores lógicos and y 
el operador de división entera %.
'''
numero = int(input("ingresar numero: "))

if  numero % 2 == 0 and numero % 7 == 0:
  print(f"el numero {numero} es par y divisible por 7")
else:
    print(f"el numero {numero} no es par o divisible por 7")

'''PUNTO DOS
Operadores matemáticos: Escribí un código para que 
un usuario ingrese dos números e imprima la suma, 
resta, multiplicación y división.
''' 
numeroUno = int(input("ingresar numero: "))
numeroDos = int(input(f"ingresar numero para sumar, restar, multiplicar y dividir al numero {numeroUno}: "))

print(f"los resultados son: \nSuma: {numeroUno + numeroDos}\nResta: {numeroUno - numeroDos}\nMultiplicacion: {numeroUno * numeroDos}\nDivision: {numeroUno / numeroDos}")

#PUNTO TRES ¿Cómo harías para saber si un número es mayor a otro?
if numeroUno > numeroDos: 
  print(f"el numero uno ({numeroUno}) es mayor al numero dos({numeroDos})")
else:
    print(f"el numero dos ({numeroDos}) es mayor al numero uno({numeroUno})")