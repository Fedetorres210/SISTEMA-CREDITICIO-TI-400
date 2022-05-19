import requests
from bs4 import BeautifulSoup
import datetime

def webScrapper(url,selector):
    res = requests.get(url)
    html = BeautifulSoup(res.text)
    table =  html.select(selector)
    return table

def separadorColumnasYDatos(table):
    columns = []
    data = []
    for elem in table:
        try:
            if int(elem.get_text()) > 2000:
                columns.append(elem.get_text())
        except:
            data.append(elem.get_text().replace(",","."))
    return columns, data

def separadorDataTBP(datos):
    data = []
    index = []
    for elem in datos:
        try:
            if float(elem) > 0:
                data.append(elem)
        except:
            if elem != '':
                index.append(elem)
    # Eliminacion de los datos del 29 de Febrero             
    data.pop(59*12)
    data.pop(59*12)
    data.pop(59*12)
    return  data



def creacionMatrizTBP(data,columns):
    matrix =  []
    index = len(columns)-1
    hoy = datetime.datetime.now()
    numero_dia = (hoy - datetime.datetime(hoy.year, 1, 1)).days + 1
    while index < len(data):
        if len(matrix) >= numero_dia:
            break
        matrix.append(data[index])
        index += len(columns)
    return matrix[-1]

TBIURL = "https://gee.bccr.fi.cr/indicadoreseconomicos/cuadros/frmvercatcuadro.aspx?idioma=1&codcuadro=%2017"
def encontrarTBP():
    table = webScrapper("https://gee.bccr.fi.cr/indicadoreseconomicos/cuadros/frmvercatcuadro.aspx?idioma=1&codcuadro=%2017","td.celda17>p")
    columns, data = separadorColumnasYDatos(table)
    data = separadorDataTBP(data)
    return creacionMatrizTBP(data,columns)


def separadorDataTED(datos):
    data = []
    index = []
    for elem in datos:
        try:
            if float(elem) > 0:
                data.append(elem)
        except:
            if elem != '':
                index.append(elem)
    # Eliminacion de los datos del 29 de Febrero             
    data.pop(359-5)
    return  data

def creadornMatrizTED(data,columns):
    matrix =  []
    index = len(columns)-2
    hoy = datetime.datetime.now()
    numero_dia = (hoy - datetime.datetime(hoy.year, 1, 1)).days + 1
    while index < len(data):
        if len(matrix) >= numero_dia:
            break
        if index >= 6*123:
            matrix.append(data[index])
            index += len(columns)
        else:
            matrix.append(data[index])
            index += len(columns)-1
    return matrix[-1]



def encontrarTED():
    table = webScrapper("https://gee.bccr.fi.cr/indicadoreseconomicos/Cuadros/frmVerCatCuadro.aspx?idioma=1&CodCuadro=%203141","p")
    columns, data = separadorColumnasYDatos(table)
    data = separadorDataTED(data)
    return creadornMatrizTED(data,columns)


print(encontrarTBP())
print(encontrarTED())


dolares = requests.get("https://tipodecambio.paginasweb.cr/api").json()["compra"]
