import bs4
import requests

urls = ['https://www.scalemates.com/colors/ak-3rd-generation-afv--976']

def getHtml(url: str):
    data = requests.get(url)
    print(data)
    if data.status_code == 200:
        soup = bs4.BeautifulSoup(data.text, "html.parser")
        print(soup)

def run():
    for x in urls:
        getHtml(x)

run()