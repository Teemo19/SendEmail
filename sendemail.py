#!/usr/bin/env python
# -*- coding: utf-8 -*-
import sys
import argparse
import smtplib
from email.MIMEMultipart import MIMEMultipart
from email.MIMEText import MIMEText
dirBcolors='/home/pi/Style/'
sys.path.append(dirBcolors)
from bcolors import bcolors

if __name__ == '__main__':
        parser=argparse.ArgumentParser()
        parser.add_argument("-txt",nargs="*",dest="Text",help="Ingresa el Texto",default="Por favor ingresa un texto")
        parser.add_argument("-to",nargs="*",dest="To",help="Ingresa el Texto",default="Por favor ingresa un texto")
        parser.add_argument("-s",nargs="*",dest="Subject",help="Ingresa un asunto",)

        result=args=parser.parse_args()

def ListToStr(list):
        try:
                return ' '.join(list)
        except:
                pass
class email:
        From=open("/usr/local/pass/from_email_sender","r").read()#Email
        To=ListToStr(result.To)
        Subject=ListToStr(result.Subject)
        Pass=open("/usr/local/pass/pass_email_sender","r").read()#Email Password
        Text=ListToStr(result.Text)

def Sender():
        try:
                msg = MIMEMultipart()
                msg['From'] = email.From
                msg['To'] = email.To
                msg['Subject'] = 'your_subject'
                msg.attach(MIMEText(email.Text, 'plain'))
                server = smtplib.SMTP('smtp.gmail.com', 587)
                server.ehlo()
                server.starttls()
                server.login(email.From,email.Pass)
                server.sendmail(email.From, email.To,msg.as_string())
                server.close()
        except:
                print(bcolors.FAIL+"NO HA INGRESADO TODOS LOS PARAMETROS REQUERIDOS"+bcolors.ENDC)
                pass
Sender()


