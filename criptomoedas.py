from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import html5lib
try:
    html = urlopen("https://www.infomoney.com.br/cryptos/bitcoin")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    Nome = res.findAll(attrs={'class':'crypto__ticker-item-name'}) 
    Cotacao = res.findAll(attrs={'class':'crypto__ticker-item-quote'})  
    Var = res.findAll(attrs={'class':'crypto__ticker-item-var'})
    
    for N, C, V in zip(Nome, Cotacao, Var):
     print(N.text.strip(),":",C.text.strip(),"("+V.text.strip()+")")