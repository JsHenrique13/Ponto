import smtplib
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
from email.mime.base import MIMEBase
from email import encoders
from random import randint
from time import sleep






def ValidaUser(email):

    destino = email
        
    emailenv = "atendimento@assesi.com"
    
    msg = MIMEMultipart()

    msg['From'] = emailenv
    msg['To'] = destino
    msg['Subject'] = "Validação de Usuário"
    chave = randint(000000, 999999)
    body = f"""
        <h1>Sua chave é {chave}</h1>
        """
    
    msg.attach(MIMEText(body, 'html'))

    server = smtplib.SMTP('smtp.gmail.com', 587)    # setando conexçao com o host do gmail
    server.starttls()   # iniciando a conexão
    server.login(emailenv, "yplqyqrmkvhzpfnp")  # logando com o email que vai enviar o email
    text = msg.as_string()  # codificando as informações pro formato de leitura do gmail
    server.sendmail(emailenv, destino, text)  # enviando as informações
    server.quit()   # fechando conexçao com o servidor
    return chave


a = ValidaUser('pinheiro012345@gmail.com')

print(a)