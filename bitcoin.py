from urllib.request import urlopen
from urllib.error import HTTPError
from urllib.error import URLError
from bs4 import BeautifulSoup
import html5lib
try:
    html = urlopen("https://dolarhoje.com/bitcoin-hoje/")
except HTTPError as e:
    print(e)
except URLError:
    print("Server down or incorrect domain")
else:
    res = BeautifulSoup(html.read(),"html5lib")
    Site = res.title.string  
    ValorB = res.find(id="nacional") 
    print ("No site * "+Site+ "* o valor do Bitcoin hoje é de "+ValorB['value'])

   
