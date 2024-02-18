import bs4
import requests
import urllib
import os
urls = ['https://www.scalemates.com/colors/italeri-acrylic-paint--678',
        'https://www.scalemates.com/colors/ak-3rd-generation-afv--976',
        'https://www.scalemates.com/colors/revell-aqua-color--654']

def getHtml(url: str):
    data = requests.get(url)
    print('Current url')
    if data.status_code == 200:
        try:
            soup = bs4.BeautifulSoup(data.text, "html.parser")
            allNews = soup.findAll('div', class_= 'ac dg bgl cc pr mt4')
            for product in allNews:
                product_name = product.find('span', class_='bgb nw').text
                series_info = product.find('div', class_='ut').text
                finish_type = product.find('div', class_='ccf center dib nw bgn').text
                paint_type = product.find('div', class_='cct center dib nw bgb').text
                style_attribute = product.find('div', class_='pr dib')['style'].split(':')[-1]
                print(f"Product Name: {product_name}")
                print(f"Series Info: {series_info}")
                print(f"Finish Type: {finish_type}")
                print(f"Paint Type: {paint_type}")
                print(f"Color Name: {style_attribute}")
                print('\n\n')
        except:
            pass
def run():
    for x in urls:
        getHtml(x)

run()

