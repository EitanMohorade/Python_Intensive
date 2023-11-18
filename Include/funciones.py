
import pandas as pd
'''
    Una función que reciba como parámetro 
    un DataFrame y nos devuelva el promedio
    de una columna en específico.
'''
def promedio_columna(dataframe, columna):
    if columna in dataframe.columns:
        suma = dataframe[columna].sum()
        return suma/dataframe[columna].count()
    else:
        return "esa columna no existe"
'''
    Una función que a todos las cadenas de
    caracteres que se tengan 
    en el DataFrame, estén con todos sus
    caracteres en minúscula.
'''
def hacer_minusucula(dataframe):
    for x in dataframe:
        dataframe[x] = dataframe[x].str.lower()
    return dataframe
'''
    Una función que reciba una DataFrame 
    y nos devuelve un diccionario con la
    cantidad de veces que se repite un valor.
'''
def valor_repetido(dataframe):
    diccionario = {}
    
    for x in dataframe.columns:
        counts = dataframe[x].value_counts().to_dict()
        diccionario[x] = counts

    resultado_df = pd.DataFrame(diccionario)

    return resultado_df
