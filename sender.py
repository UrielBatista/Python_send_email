import smtplib


import os
import imghdr


from email.message import EmailMessage


MY_ADDRESS = 'email_destino'
PASSWORD = 'senha'
# YOU = ['email_enviado_1', 'email_enviado_2']
YOU = 'email_destino_unico'

msg = EmailMessage()
# msg = MIMEMultipart('alternative')
msg['Subject'] = "Link"
msg['From'] = MY_ADDRESS
msg['To'] = YOU


# corpo da menssagem
text = "Imagem rendenizada!!"
# with open('0.png', 'rb') as f:
#   file_data = f.read()
#   file_type = imghdr.what(f.name)
#   file_name = f.name

# msg.add_attachment(file_data, maintype='image', subtype=file_type, filename=file_name)



html_message = open('teste.html').read()
msg.add_alternative(html_message, subtype='html')


#################################################################################################################################################
# with open('bord1.png', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

# with open('bord2.png', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

# with open('bord3.png', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)
#################################################################################################################################################

# with open('img4.jpg', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

# with open('img5.jpg', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)

# with open('mdb-email.png', 'rb') as attach_file:
#     image_name = attach_file.name
#     image_type = imghdr.what(attach_file.name)
#     image_data = attach_file.read()

# msg.add_attachment(image_data, maintype="image", subtype=image_type, filename=image_name)




# connectando com o smtp
s = smtplib.SMTP(host='smtp_do_email_destino', port=porta_do_smtp)
s.starttls()
s.login(MY_ADDRESS, PASSWORD)
print('Terminando!!!')
# Desconectando com o smtp
s.sendmail(MY_ADDRESS, YOU, msg.as_string())
s.quit()
