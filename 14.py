# write a function which will be able to access your mail .
#https://docs.python.org/3/library/email.message.html#email.message.EmailMessage.walk

import imaplib,email,getpass

def mail():
    """Read your mailbox"""
    USER_NAME = input("Enter your email address\n")
    PASSWORD = getpass.getpass()
    print("Enter the IAMP server.Ex-For gmail - imap.gmail.com,For outlook-outlook.office365.com")
    server = input()
    prompt = input("Do you want HTML to be shown in terminal? Type Yes or No\n")
    with imaplib.IMAP4_SSL(server,993) as imap_server:
        imap_server.login(USER_NAME,PASSWORD)
        imap_server.select("inbox",readonly=True)
        result,data = imap_server.search(None,"ALL")
        data = data[0].split()
        data = list(reversed(data))
        print(f"total number of mail in inbox is {len(data)}")
        x = int(input("Enter the number of mails that you want to display\n"))
        for i in data[:x]:
            tmp,mail_data = imap_server.fetch(i,'(RFC822)')
            # print(mail_data)
            tmp,mail_data = mail_data[0]
            mail_msg = email.message_from_bytes(mail_data)
            # msg_head = email.header.make_header(email.header.decode_header(mail_msg['Subject']))
            msg_head = mail_msg['Subject']
            print(f"To : {mail_msg['To']}")
            print(f"From : {mail_msg['From']}\nDate : {mail_msg['Date']}")
            msg_head = str(msg_head)
            print("Subject: {}".format(msg_head))
            if prompt.lower() == "no":
                for element in mail_msg.walk():
                    if element.get_content_type() == "text/plain" :
                        element = str(element)
                        print(element)
            elif prompt.lower() == "yes":
                for element in mail_msg.walk():
                    if element.get_content_type() == "text/plain" or element.get_content_type() == "text/html":
                        element = str(element)
                        print(element)
            else:
                print("Error")
                break

if __name__ == "__main__":
    mail()