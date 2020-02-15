#!/usr/bin/env python3

import smtplib

#send email from python
#this creates a text email and sends it to an address of your choosing directly from python
def mailsend (toaddress,fromaddress,subject,message):
    #you need to know your correct smtp server for this to work, mine is in the function below
    smtpserver = smtplib.SMTP("smtp.east.cox.net",25)
    header = 'To:' + toaddress + '\n' + 'From:' + fromaddress + '\n' + 'Subject: ' + subject +'\n'
    msg = header + '\n' + message
    smtpserver.sendmail(fromaddress, toaddress, msg)
    smtpserver.close()
"""   
the below calls the function - you should change the address settings for your purposes, and you can change the subject and message details as well to send the message information you want to send
"""
mailsend (' recipient@address.com',' sender@address.com','test from python','this is the test message') 