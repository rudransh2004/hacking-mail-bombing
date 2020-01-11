import smtplib
import random
import os
from pyfiglet import Figlet
import time
import pyttsx3




def clr():
    if os.name == 'nt':
        os.system('cls')
    else:
        os.system('clear')




def banner():
    clr()
    custom_fig = Figlet(font='graffiti')
    print(custom_fig.renderText('SHIVAAY'))
    
                       
def mail():
    engine = pyttsx3.init()
    server = smtplib.SMTP_SSL('smtp.gmail.com', 465)
    server.login("joy86591@gmail.com","10feb1981")
    
    engine.say("enter your targets email address")
    engine.runAndWait()
    time.sleep(0.1)
    target_email = input("ENTER THE EMAIL ADDRESS OF TARGET:")
    engine.say("enter the message you want to send:")
    engine.runAndWait()
    time.sleep(0.1)
    body = str(input("ENTER THE BODY OF THE MAIL:"))
    engine.say("please tell that how many number of mails you want to send")
    engine.runAndWait()
    time.sleep(0.1)
    no = int(input("ENTER THE NO OF MAILS YOU WANT TO SEND:"))
    
    for i in range(0,no):
        print("REQUEST OF MAILS HAS BEEN SENT:",i)
        server.sendmail("joy86591@gmail.com",
                        target_email,
                        body)
        
    server.quit() 
   
    
    
    
banner()
time.sleep(1)
mail()    
    
    
    
    
    
    
                     
                       
                       