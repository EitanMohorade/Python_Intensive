import yagmail

'''
    devolverá
    dos variables: mail
    y contraseña.
'''
#puse contrasenia sin enie por las dudas
def usuario_contrasenia(ruta):
    datos = []
    archivo = open(ruta, 'r')
    datos.append(archivo.read())
    archivo.close()
    return datos

'''
    Una función que se llame: enviar_mail. Esta función 
    utiliza la librería yagmail.
    Recibirá los datos: mail, contraseña, asunto,
    mensaje, destinatarios. La función
    utilizará mail y contraseña para enviar un mail, 
    para el asunto utilizará la variable
    asunto y para el cuerpo del mail, mensaje. El mail lo 
    enviará a la lista de destinatario
    en destinatarios.
'''
def enviar_mail(mail, contrasenia, asunto, mensaje, destinatarios):
    yag = yagmail.SMTP(user=mail, password=contrasenia)
    return yag.send(destinatarios, asunto, mensaje)