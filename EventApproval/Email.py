
import smtplib
import imghdr
from email.message import EmailMessage

def SendEmail(To, eventName, date):
    msg = EmailMessage()
    msg['Subject'] = 'Request for Event Approval'
    #msg['Subject'] = 'Test mail- with attachment'
    msg['From'] = str('Your Email Address')
    msg['To'] = str(To)
    msg.set_content('We are supposed to conduct '+ str(eventName) + ' on ' + str(date) + '. Please accept our permission letter. We have attached our poster.\n\nRegards,\nXYZ')
    #msg.set_content('Check out this really cute puppy!')

    files = ['ISA-logo-jpg.jpg']
    #
    for file in files:
          with open(file, 'rb') as f:
              file_data = f.read()
              file_type = imghdr.what(f.name)
              file_name = f.name

          msg.add_attachment(file_data,maintype='image',subtype=file_type,filename = file_name)

    with smtplib.SMTP_SSL('smtp.gmail.com', 465) as smtp:
           smtp.login('YourEmailAddress', 'YourPassword')
           smtp.send_message(msg)

SendEmail('2018.raj.talashilkar@ves.ac.in', 'Django Workshop', '10th and 11th April, 2021')
SendEmail('2018.omkar.mangalpalli@ves.ac.in', 'Django Workshop', '10th and 11th April, 2021')
SendEmail('2018.jatin.dandelia@ves.ac.in', 'Django Workshop', '10th and 11th April, 2021')
