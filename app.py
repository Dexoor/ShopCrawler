# created by: Dexoor
# contact: daniel.walaszek0@gmail.com

import requests
from bs4 import BeautifulSoup
import sys
import codecs
sys.stdout = codecs.getwriter('utf-8')(sys.stdout.detach())


def crawler_morele(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding='utf-8')
    price = soup.find("div", class_="product-price").getText()
    name = soup.find("h1", class_='prod-name').getText()
    shop = url[12:22]
    print(f'{shop} -> {name}' + price)


def crawler_xkom(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding='utf-8')
    price = soup.find("div", class_="u7xnnm-4 jFbqvs").getText()
    name = soup.find("h1", class_='sc-1bker4h-4 driGYx').getText()
    shop = url[12:20]
    print(f'{shop} -> {name}'+'\n' + price+'\n')


def crawler_amazon(url):
    headers = {
        "User-Agent": 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/90.0.4430.212 Safari/537.36'
    }
    page = requests.get(url, headers=headers)
    soup = BeautifulSoup(page.content, "html.parser", from_encoding='utf-8')
    price = soup.find(id="priceblock_ourprice").getText()
    name = soup.find("span", id='productTitle').get_text()
    shop = url[12:21]

    print(f'{shop} -> {name.strip()} '+'\n' + price+'\n')


crawler_morele(
    "https://www.morele.net/procesor-amd-ryzen-5-5600x-3-7ghz-32-mb-box-100-100000065box-7267026/")
crawler_morele(
    'https://www.morele.net/procesor-amd-ryzen-5-5600x-3-7ghz-32-mb-oem-100-100000065mpk-5947227/')
crawler_xkom(
    'https://www.x-kom.pl/p/597427-procesor-amd-ryzen-5-amd-ryzen-5-5600x.html')
crawler_amazon(
    'https://www.amazon.pl/gp/product/B08166SLDF/ref=ox_sc_act_title_2?smid=A35Y6JPOM42WES&psc=1')
crawler_morele(
    'https://www.morele.net/pamiec-hyperx-fury-ddr4-16-gb-3600mhz-cl17-hx436c17fb3k2-16-6465944/')
crawler_amazon('https://www.amazon.pl/HyperX-HX436C17FB3K4-64-pami%C4%99%C4%87-robocza/dp/B083Q4R4HH/ref=sr_1_2?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Pami%C4%99%C4%87%2BHyperX%2BFury%2C%2BDDR4%2C%2B16%2BGB%2C%2B3600MHz%2C%2BCL17&qid=1621533545&sr=8-2&th=1')
crawler_morele(
    'https://www.morele.net/plyta-glowna-gigabyte-b550m-aorus-elite-7005841/')
crawler_amazon('https://www.amazon.pl/GIGABYTE-B550M-AORUS-ELITE-procesor%C3%B3w/dp/B08BN8VD23/ref=sr_1_1?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=P%C5%82yta+g%C5%82%C3%B3wna+Gigabyte+B550M+AORUS+ELITE&qid=1621533598&sr=8-1')
crawler_morele(
    'https://www.morele.net/zasilacz-silentiumpc-vero-m3-700w-spc269-5942218/')
crawler_amazon('https://www.amazon.pl/SilentiumPC-Vero-L3-Stromversorgung-700/dp/B08XNLL9LV/ref=sr_1_4?__mk_pl_PL=%C3%85M%C3%85%C5%BD%C3%95%C3%91&dchild=1&keywords=Zasilacz+SilentiumPC&qid=1621533710&sr=8-4')
