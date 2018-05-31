import smtplib
import time
import imaplib
import email
import getpass
import pprint
import mail

GMAIL_USER = 'np.lab4@gmail.com'
GMAIL_PWD = 'Laboratorul4'

M = imaplib.IMAP4_SSL('imap.gmail.com')

def lastNReceived(n):
    #try:
        #M.select('INBOX',True)
        rv, data = M.search(None, 'ALL')
        if rv != 'OK':
            print ("No messages found!")
            return
        print (data)


try:
    M.login(GMAIL_USER, GMAIL_PWD)
except imaplib.IMAP4.error:
    print ("LOGIN FAILED!!! ")
    sys.exit(1)


M.list()
M.select('INBOX',True)


unread_messages = mail.numberOfUnreadMessages(M)
print('Unseen: ', unread_messages)

n = int(input('give number of emails to display : '))
mail.lastNMsg(M, n-1)

print('Short preview of all mails: ')
mail.getBody(M)

i = int(input('Choose mail to dispay : '))
mail.choosedMsg(i-1)

mail.sendMail(GMAIL_USER, GMAIL_PWD)
print('mail send')

print('done')
M.logout()


