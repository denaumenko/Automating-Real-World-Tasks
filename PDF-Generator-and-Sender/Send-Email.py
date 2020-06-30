from email.message import EmailMessage
import smtplib
import getpass

mail_server = smtplib.SMTP('localhost')
# mail_server = smtplib.SMTP_SSL('smtp.example.com')
# mail_server.set_debuglevel(1)
# mail_pass = getpass.getpass('Password? ')
# mail_server.login(sender, mail_pass)
# mail_server.quit()

message = EmailMessage()

sender = "me@example.com"
recipient = "you@example.com"

message['From'] = sender
message['To'] = recipient
message['Subject'] = 'Greetings from {} to {}!'.format(sender, recipient)
message.set_content("Hey there")
print(message)
