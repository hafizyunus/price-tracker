
# FOR NEW PRODUCT
#   UPDATE URL -- line 41
#   UPDATE PRICE LENGTH -- in get_price() line 81


from tkinter import ttk, BOTH, Menu, RIGHT, CENTER, LEFT, W, E, N, S, TclError, Listbox, END
from ttkthemes import ThemedTk

import requests
from datetime import datetime
from bs4 import BeautifulSoup

class priceCheck:
    
    def __init__(self, master):

        master.title('Price Checker')

        # ***** Frames *****

        self.mainFrame = ttk.Frame(master, width=500, height=500)
        self.mainFrame.pack(fill=BOTH)

        # ***** Styles *****

        style = ttk.Style(mainWin)
        style.configure('TButton', font=('Helvetica', 20), padding=10)
        style.configure('S.TButton', font=('Helvetica', 17), padding=7)
        style.configure('TEntry', padding=5)
        style.configure('TLabel', font=('Courier', 15), padding=10)
        style.configure('B.TLabel', font=('Courier', 15, 'bold'), padding=10)
        style.configure('L.TLabel', font=('Courier', 20), padding=10)

        self.font = 'Helvetica 15'
        self.Lfont = 'Helvetica 20'

        # ***** Random Variables *****

        URL = '' # Product link
        headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

        # ***** Main Window *****

        self.dateTime = ttk.Label(self.mainFrame, text=self.get_dateTime(), style='TLabel', justify=CENTER, anchor=W)
        self.dateTime.grid(row=1, column=1, padx=5, pady=10, sticky=W+E+N+S)

        self.name = ttk.Label(self.mainFrame, text=self.get_title(URL, headers), style='TLabel', justify=CENTER, anchor=CENTER)
        self.name.grid(row=2, column=1, padx=5, pady=5, sticky=W+E+N+S)

        self.price = ttk.Label(self.mainFrame, text=self.get_price(URL, headers), style='TLabel', justify=CENTER, anchor=CENTER)
        self.price.grid(row=3, column=1, padx=5, pady=5, sticky=W+E+N+S)

        self.update = ttk.Button(self.mainFrame, text='Update', style='TButton', command=lambda: self.updatePrice(URL, headers), width=15)
        self.update.grid(row=4, column=1, padx=5, pady=5, sticky=W+E+N+S)

        self.quit = ttk.Button(self.mainFrame, text='Quit', style='S.TButton', command=master.destroy, width=4)
        self.quit.grid(row=5, column=1, padx=5, pady=20)

        self.lSpace = ttk.Label(self.mainFrame, width=1)
        self.lSpace.grid(row=0, column=0, pady=0)

        self.rSpace = ttk.Label(self.mainFrame, width=1)
        self.rSpace.grid(row=6, column=3, pady=0)

    # ***** Functions *****

    def get_title(self, URL, headers):
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        title = soup.find(id='productTitle').get_text().strip()
        if len(title) > 40:
            title = title[:40]
        return title

    def get_price(self, URL, headers):
        page = requests.get(URL, headers=headers)
        soup = BeautifulSoup(page.content, 'html.parser')

        price = soup.find(id='priceblock_ourprice').get_text()
        converted_price = eval(price[2:9]) # Number part of price (returns tuple split on commas)
        #price = eval(soup.find_all('span', class_='total--sale-price')[0].contents[0])  #for span elements
        converted_price = converted_price[0]*1000 + converted_price[1] #converts tuple to numeric
        return converted_price

    def get_dateTime(self):
        now = datetime.now()
        dateTime = now.strftime("%d/%m/%Y %H:%M:%S")
        return dateTime

    def updatePrice(self, URL, headers):
        title = self.get_title(URL, headers)
        price = self.get_price(URL, headers)
        dateTime = self.get_dateTime()

        self.dateTime.config(text=dateTime)
        self.name.config(text=title)
        self.price.config(text=price)



mainWin = ThemedTk(theme='arc')
mainWin.resizable(False,False)
#mainWin.geometry('500x500+200+150')
priceCheck(mainWin)
mainWin.mainloop()