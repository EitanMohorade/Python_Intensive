import funciones as func

listaComunasDenuncias = ["Villa del parque", "Almagro", "Retiro", "Retiro", "Retiro"]
comunas_sin_repetir = list(set(listaComunasDenuncias))

print("Elegir comuna y su cantidad de denuncias respectivas sobre la falta de parques\nOPCIONES:")
for x in comunas_sin_repetir:
    print(f"{x}")

comuna = input("Ingresa el nombre de la comuna tal cual está escrito: ")
funcion2 = func.contar_cadena(listaComunasDenuncias, comuna)
print(f"Denuncias en la comuna {comuna} sobre falta de parques en su zona: {funcion2}")

print("//////////////////////////////////")

listaComunasNum = [14, 14, 14, 14, 4, 4, 7, 11, 10, 9, 12 , 11, 1, 1 , 5, 6, 15, 2, 3, 13]
comunaNum = int(input("Ingresa el numero de comuna del 1 al 15 de CABA: "))
funcion1 = func.contar_valor(listaComunasNum, comunaNum)
#funcion1Ver2 = func.contar_valorVer2(listaNum, 3) FUNCIONA
print (f"Personal de la comuna {comunaNum}: {funcion1}")

print("//////////////////////////////////")

fechaDeNacimiento = input("para calcular la edad de algun funcionario.\ningresar su dia de nacimiento con este formato: dia-mes-year\n")
funcion3 = func.calcular_edadVer2(fechaDeNacimiento)
print(f"la edad es: {funcion3}")