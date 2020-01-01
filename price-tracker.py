
# FOR NEW  PRODUCT
#   UPDATE URL
#   UPDATE PRICE LENGTH

# BEFORE USING THE MAIL STUFF
#   TURN ON LESS SECURE APPS
#   ENTER TO AND FROM MAIL IN sendMail()
#   ENTER ACCOUNT PASSWORD

import requests
from bs4 import BeautifulSoup
import smtplib
from datetime import datetime
import time

URL = 'https://www.amazon.in/AmazonBasics-21-Ltrs-Classic-Backpack/dp/B013TGESIQ?pf_rd_p=bcb4cee7-28fc-4e80-9dd2-4518c354abf0&pd_rd_wg=Myn9T&pf_rd_r=PFASZ0GNMCTPVER5M8D1&ref_=pd_gw_unk&pd_rd_w=CAZUd&pd_rd_r=29f57772-5004-4b0c-bbe1-e678b8391224' # Product link

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def checkPrice():
    page = requests.get(URL, headers=headers)

    soup = BeautifulSoup(page.content, 'html.parser')

    title = soup.find(id='productTitle').get_text()
    price = soup.find(id='priceblock_ourprice').get_text()
    converted_price = float(price[1:5]) # Number part of price

    if converted_price < 850:
        updateFile(converted_price)
        #sendMail()
    #print(converted_price)
    #print(title.strip())

def updateFile(price):
    now = datetime.now()
    dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
    file = open(r'D:\My Stuff\VSCode\Python\misc\pricelist.txt','a')
    file.write('Price: ' + str(price) + ', ' + dt_string)
    print('updated')

def sendMail():
    server = smtplib.SMTP('smtp.gmail.com', 587)
    server.ehlo()
    server.starttls()
    server.ehlo()
    
    server.login('hafizy007@gmail.com', '') # Secord arg is password

    subject = 'Price fell down'
    body = 'Check  ' + URL

    msg = f'Subject: {subject}\n\n{body}'

    server.sendmail(
        '', # From mail id
        '', # To mail id
        msg
    )

    server.quit()

while True:
    checkPrice()
    time.sleep(60*60*24)