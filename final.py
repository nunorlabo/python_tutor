import smtplib
from email.mime.text import MIMEText 
from email.utils import formatdate


class Mailer():

    myAddr = "********@example.com"
    myPass = "********"
    subject = ""
    destAddr = ""
    message = ""

    def __init__(self):
        self.smtpobj = smtplib.SMTP('smtp.gmail.com', 587) 
        self.smtpobj.ehlo() 
        self.smtpobj.starttls() 
        self.smtpobj.ehlo() 
        self.smtpobj.login(self.myAddr, self.myPass)

    def __del__(self):
        self.smtpobj.close()

    def setSubject(self, subject):
        self.subject = subject

    def setDestAddr(self, destAddr):
        self.destAddr = destAddr

    def setMessage(self, message):
        self.message = message

    def sendMail(self):
        isValid = True
        if self.subject == "":
            print("Put in your email's subject.")
            isValid = False
        if self.destAddr == "":
            print("Put in your email's destination.")
            isValid = False
        if self.message == "":
            print("Put in your message.")
            isValid = False
        if not isValid:
            return
        msg = MIMEText(self.message) 
        msg['Subject'] = self.subject
        msg['From'] = self.myAddr
        msg['To'] = self.destAddr 
        msg['Date'] = formatdate()
        self.smtpobj.sendmail(self.myAddr, self.destAddr, msg.as_string()) 
        

mailer = Mailer()
mailer.setSubject("おはよう")
mailer.setDestAddr("********@gmail.com")
mailer.setMessage("起きろ")
mailer.sendMail()