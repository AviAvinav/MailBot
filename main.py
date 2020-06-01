import smtplib as smt

def send_email(subject, msg):
    try:
        server = smt.SMTP('smtp.gmail.com:587') #change it according to your convenience.
        server.ehlo()
        server.starttls()
        server.login("Enter your email", "Enter your password here")
        message = 'Subject: {}\n\n{}'.format(subject, msg)
        server.sendmail("Enter your email","Enter the email the mail is to be sent to", message)
        server.quit()
        print("E-mail sent")
    except:
        print("E-mail not sent")

sub = "Sent from PyProg" #change the subject according to your will.
msge = "Enter your message here."

send_email(sub, msge)
