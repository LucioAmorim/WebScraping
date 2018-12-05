from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import html5lib
try:
    html = urlopen("https://turcambio.com.br/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    Nome = res.findAll(attrs={'class':'nome-moeda'}) 
    Cotacao = res.findAll(attrs={'class':'valor-atual-sobec'})  

    for N, C in zip(Nome, Cotacao):
     print(N.text.strip(),":",C.text.strip())