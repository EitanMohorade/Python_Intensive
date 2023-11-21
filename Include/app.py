import pandas as pd
import graficos
import travel_data as email


path_txt = 'C:/Users/Lochofo/Desktop/PAGINAS/Python_Intensive/dsd8y9/Include/email.txt'
path = "C:/Users/Lochofo/Desktop/PAGINAS/Python_Intensive/dsd8y9/Include/integrados_8_y_9.xlsx"
respuestas = pd.read_excel(path)
pd.set_option('display.max_rows', None)
pd.set_option('display.max_columns', None)

arboles_xcuadra = respuestas["Cuantos arboles hay en su cuadra? (aprox)"].value_counts()
tachos_xcuadra = respuestas["Cuantos tachos de basura hay en su cuadra?"]

#graficos.grafico_barra(arboles_xcuadra, "Respuestas", "Frecuencia", "Porcentaje de respuestas sobre arboles por cuadra", 'm')

#graficos.grafico_comun(tachos_xcuadra, "Respuesta", "Frecuencia", "Cantidad de tachos de basura por cuadra")

destinatarios = []

for  destino in respuestas["Email"]:
    if pd.notna(destino):
        destinatarios.append(destino)

datos = email.usuario_contrasenia(path_txt)

email.enviar_mail(datos[0], datos[1], "prueba asunto", "preguba mensaje", destinatarios)