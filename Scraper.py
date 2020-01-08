import requests
from bs4 import BeautifulSoup
import smtplib


URL = 'https://www.amazon.fr/Canon-Appareil-num%C3%A9rique-Objectif-Reconditionn%C3%A9/dp/B01M655CBB/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3R40D9E615N56&keywords=canon+450d&qid=1578476175&sprefix=canon+450%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTVgzSU9STTk3NFdSJmVuY3J5cHRlZElkPUEwMDU3OTMwM0EwTFU0OVoxQUUySSZlbmNyeXB0ZWRBZElkPUEwODE4MjM3NVlKVVNWTURWMk4wJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='

headers ={"User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/79.0.3945.88 Safari/537.36'}

def check_price():
   page = requests.get(URL, headers=headers)

   soup = BeautifulSoup(page.content, 'html.parser')

   title = soup.find(id="productTitle").get_text()
   price = soup.find(id="priceblock_ourprice").get_text()
   converted_price = float(price[0:5].replace(',', '.'))

   if(converted_price <300):
     send_mail()

   print(converted_price)
   print(title.strip())

   if(converted_price > 100):
     send_mail()

def send_mail():
    server = smtplib.SMTP('smtp.gmail.com',587)
    server.ehlo()
    server.starttls()
    server.ehlo()

    server.login('enter email','enter password')
    subject = ' Price fell down!'
    body = 'check the amazon link  https://www.amazon.fr/Canon-Appareil-num%C3%A9rique-Objectif-Reconditionn%C3%A9/dp/B01M655CBB/ref=sr_1_1_sspa?__mk_fr_FR=%C3%85M%C3%85%C5%BD%C3%95%C3%91&crid=3R40D9E615N56&keywords=canon+450d&qid=1578476175&sprefix=canon+450%2Caps%2C189&sr=8-1-spons&psc=1&spLa=ZW5jcnlwdGVkUXVhbGlmaWVyPUEzTVgzSU9STTk3NFdSJmVuY3J5cHRlZElkPUEwMDU3OTMwM0EwTFU0OVoxQUUySSZlbmNyeXB0ZWRBZElkPUEwODE4MjM3NVlKVVNWTURWMk4wJndpZGdldE5hbWU9c3BfYXRmJmFjdGlvbj1jbGlja1JlZGlyZWN0JmRvTm90TG9nQ2xpY2s9dHJ1ZQ=='
    msg = f"Subject : {subject}\n\n{body}"
    server.sendmail(
         'enter email1',
         'enter email2',
         msg
    )
    print('HEY EMAIL HAS BEEN SENT!')
    server.quit()
    

check_price()