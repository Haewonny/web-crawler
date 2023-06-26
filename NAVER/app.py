import requests
import urllib.request

from bs4 import BeautifulSoup

''' 삼성전자, LG전자, 현대차, 카카오, LG디스플레이, 대한항공'''
stocks = ['005930', '066575', '005380', '035720', '034220', '003490']

def 현재가(num):
    data = requests.get(f'https://finance.naver.com/item/sise.nhn?code={num}')

    soup = BeautifulSoup(data.content, 'html.parser')

    return soup.find_all('strong', id="_nowVal")[0].text

file = open('stock.txt', 'w') # write mode
for x in stocks:
    file.write('\n' + 현재가(x))

file.close()