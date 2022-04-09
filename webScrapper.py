import requests
from bs4 import BeautifulSoup

TBIURL = "https://gee.bccr.fi.cr/indicadoreseconomicos/cuadros/frmvercatcuadro.aspx?idioma=1&codcuadro=%2017"

res = requests.get(TBIURL)
print(res.text)
