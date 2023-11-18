import yagmail

email = ""
password = ""

yag = yagmail.SMTP(user=email, password=password)
destino = ['']

asunto = ''
msj = ""
titulo = ""

yag.send(destino, asunto, [titulo, msj])