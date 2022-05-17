import smtplib

def mandarCorreoElectronico(email,mensaje):
    subject = "Credito"
    message = "Subject: {}\n\n{}".format(subject, mensaje)
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.starttls()
    server.login("creditobancario.proyecto@gmail.com", "ProyectoProgra01234")
    server.sendmail("creditobancario.proyecto@gmail.com", email, message)
    server.quit() 
    return True
