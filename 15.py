import smtplib,getpass
# https://docs.python.org/3/library/smtplib.html
# https://docs.python.org/3/library/getpass.html

prompt = """press 1 for @gmail.com\npress 2 for @outlook.com\npress 3 for others\n"""
mailinput = input(prompt)
USER_NAME = input("Enter your email address\n")
PASSWORD = getpass.getpass()
Receiver_mail = input("Enter mail of recipient\n")
subject = input("Enter the subject of the mail\n")
body = input("Enter the body of the mail\n")
msg = f"Subject :{subject}\n\n{body}"
class mail:
    def __init__(self,host,port):
        self.host = host
        self.port = port
    def __str__(self):
        return "Send mail to anyone"
    def mail_SSL(self):
        """Send mail if SSL"""
        try:
            with smtplib.SMTP_SSL(self.host,self.port) as server:
                server.login(USER_NAME,PASSWORD)
                server.sendmail(USER_NAME,Receiver_mail,msg)
        except Exception as e:
            print(e)
    def mail_TLS(self):
        """Send mail if TLS"""
        try:
            server = smtplib.SMTP(self.host,self.port)
            server.ehlo() # Can be omitted
            server.starttls() # Secure the connection
            server.ehlo() # Can be omitted
            server.login(USER_NAME,PASSWORD)
            server.sendmail(USER_NAME,Receiver_mail,msg)
        except Exception as e:
            print(e)
        finally:
            server.quit() 

def drivercode():
    """can send mail to anyone using mail class"""
    if mailinput == "1":
        x = input("Enter 1 for SSL or 2 for TLS")
        if x == "1":
            user_mail = mail("smtp.gmail.com",465) # Creating object
            user_mail.mail_SSL()
        elif x == "2":
            user_mail = mail("smtp.gmail.com",587) # Creating object
            user_mail.mail_TLS()
        else:
            print("Enter correct input")
    elif mailinput == "2":
        user_mail = mail("smtp-mail.outlook.com",587) # Creating object
        user_mail.mail_TLS()
    elif mailinput == "3":
        mail_host = input("Enter the smtp mailserver address.Ex-'smtp-mail.outlook.com'\n")
        mail_port = input("Enter the Port\n")
        mail_type = input("Enter 1 for SSL or 2 for TLS\n")
        user_mail = mail(mail_host,mail_port) # Creating object
        if mail_type == "1":
            user_mail.mail_SSL()
        elif mail_type == "2":
            user_mail.mail_SSL()
        else:
            print("Enter correct input")
    else:
        print("Enter correct input")

if __name__ == "__main__":
    drivercode()