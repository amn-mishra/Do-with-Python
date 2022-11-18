import smtplib , ssl
port = 465  # For SSL
smtp_server = "smtp.gmail.com"
sender_email =   "________@gmail.com"  # Enter your address
receiver_email = "________@gmail.com"  # Enter receiver address
password = 'luibrojetjuskbog' # for this password go to your google account setting and then click on security you'll see option app password ,generate password from there
message = """i am going to send the mail to given email id  """ #whatsoever you want to send write here 

context = ssl.create_default_context()
with smtplib.SMTP_SSL(smtp_server, port, context=context) as server:
    server.login(sender_email, password)
    server.sendmail(sender_email, receiver_email, message)


