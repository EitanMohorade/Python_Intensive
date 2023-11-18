import funciones as func
import pandas as pd

arboles_plantados = pd.DataFrame([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
])
  
print(f"Promedio de la cantidad de arboles plantados en todas las comunas: {func.promedio_columna(arboles_plantados, 2)}")

informes = { 'comuna': ['3', '14', '6', '8'],
         'estado': ['sin persOnAl', 'sin PErsonal', 'SIn peRSonal' ,'con pERSOnal']
}
df = pd.DataFrame(informes)
print(f"informe del personal segun comuna: \n{func.hacer_minusucula(df)}")



cant_problematicas = {'desagues': [1, 2, 2, 3, 3, 3, 6, 6, 4, 5, 5, 1],
        'suciedad': [4, 4, 5, 5, 5, 6, 3, 2, 2, 1, 1, 1]}

df2 = pd.DataFrame(cant_problematicas)


print(f"Segun la comuna, la cantidad de reportes de X problematicas son: \n{func.valor_repetido(df2)}")

