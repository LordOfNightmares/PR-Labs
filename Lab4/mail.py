import smtplib
import time
import imaplib
import email
import getpass
import pprint

LIST = []

def sendMail(user, pwd):
    smtpserver = smtplib.SMTP("smtp.gmail.com",587)
    smtpserver.ehlo()
    smtpserver.starttls()
    smtpserver.ehlo
    smtpserver.login(user, pwd)
    to = input('Enter receivers mail: ')
    subject = input('Enter subject: ')
    CC = input('Enter CC: ')
    header = 'From: ' + user + '\n' + 'subject: ' + subject + '\n' + 'CC: ' + CC + '\n' 
    body = input('Enter body of mail: ')
    msg = to + header + body
    smtpserver.sendmail(user, to, msg)
    smtpserver.close()



def numberOfUnreadMessages(M):
    try:
        #M.select('INBOX', True)
        rv, data = M.search(None, 'UnSeen') ####### < ---- can be used also for search
        count = (len(data[0])+1)//2
    except :
       count = 0
    return count



def getBody(M):
    attachment = 0
    msg = 0
    
    result, data = M.uid('search', None, "ALL")
    # search and return uids instead
    #i = len(data[0].split())  # data[0] is a space separate string
    for x in range(0, len(data[0].split())) :
        msg = msg + 1
        print('__________________________________________________________')
        print('Email No. ', msg)  
        latest_email_uid = data[0].split()[x] # unique ids wrt label selected
        result, email_data = M.uid('fetch', latest_email_uid, '(RFC822)')
        # fetch the email body (RFC822) for the given ID
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode()
        # converts byte literal to string removing b''
        email_message = email.message_from_string(raw_email_string)
        #print(email_message, '++++++++++++++++++++++++++++++++++++')
        # this will loop through all the available multiparts in mail
        for part in email_message.walk():
            if part.get_content_type() == "multipart/mixed":
                attachment = attachment +1
                
            elif part.get_content_type() == "text/plain": # ignore attachments/html
                body = part.get_payload(decode=True)
                print(body.decode()[0:body.decode().find('.')])
                LIST.append(body)
                # body is again a byte literal
            else:
                continue
        
    print ('Attachment(s): ',attachment)
    


def choosedMsg(i):
    print(LIST[i].decode('utf-8'))


def lastNMsg(M, n):
    result, data = M.uid('search', None, "ALL")
    for x in range(n, -1, -1) :
        latest_email_uid = data[0].split()[x] # unique ids wrt label selected
        result, email_data = M.uid('fetch', latest_email_uid, '(RFC822)')
        # fetch the email body (RFC822) for the given ID
        raw_email = email_data[0][1]
        raw_email_string = raw_email.decode()
        # converts byte literal to string removing b''
        email_message = email.message_from_string(raw_email_string)
        print('Subject: ', email_message['subject'])
        print('Date: ', email_message['date'])
        print('From: ', email_message['from'])
        print('________________')
