from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import html5lib
import re

try:
    html = urlopen("https://www.infomoney.com.br/cryptos/bitcoin")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(), "html5lib")
    Nome = res.findAll(attrs={'class': 'crypto__ticker-item-name'})
    Cotacao = res.findAll(attrs={'class': 'crypto__ticker-item-quote'})
    Var = res.findAll(attrs={'class': 'crypto__ticker-item-var'})
    Hora = res.findAll(attrs={'class': 'crypto__ticker-item-logo'})
    Hx = res.findAll('script')
    
    for N, C, V, H in zip(Nome, Cotacao, Var, Hora):
        print(N.text.strip(), ":", C.text.strip(), "(" + V.text.strip() + ")","Atualizado em :",H['title'])

    variants = res.find_all(string=re.compile(r'\[\"([^a-z]*?)\]\;'))
    for x in variants:
      print (x)
    

