from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import html5lib
try:
    html = urlopen("https://www.webmaissistemas.com.br/empresa/trabalhe")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    for Oportunidades in res.findAll(attrs={'class':'titulo'}):
        if 'Analista de Sistemas' in Oportunidades.text.strip() or 'Estágio em Design Gráfico' in Oportunidades.text.strip():
            print (Oportunidades.text.strip())