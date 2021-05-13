
# FOR NEW PRODUCT
#   UPDATE URL
#   UPDATE PRICE LENGTH

# BEFORE USING THE MAIL STUFF
#   TURN ON LESS SECURE APPS
#   ENTER TO AND FROM MAIL IN sendMail()
#   ENTER EMAIL ID AND PASSWORD 

import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time
from win10toast import ToastNotifier

checkRate = 3

URL = '' # Product link

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = eval(price[4:9]) # Number part of price
    #price = eval(soup.find_all('span', class_='total--sale-price')[0].contents[0])  for span elements
    converted_price = converted_price[0]*1000 + converted_price[1]

    if converted_price < 1100:
        pushNotification(price)
        #updateFile(price)
        #sendMail(price)
    #print(converted_price)
    #print(title.strip())

def updateFile(price):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file = open(r'D:\My Stuff\VSCode\Python\misc\pricelist.txt','a')
    file.write('Price: ' + str(price) + ', ' + dt_string)
    file.close()

def pushNotification(price):
    notify = ToastNotifier()
    notify.show_toast('Price Drop!', 'Price is now ' + str(price), duration=10)

def sendMail(price):
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('', '') # Username and Password

    subject = 'Price is now ' + price
    body = 'Check  ' + URL

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        '', # From mail id
        '', # To mail id
        msg
    )

    server.quit()

checkPrice()

'''while True:
    checkPrice()
    time.sleep(60*60*24/checkRate)'''