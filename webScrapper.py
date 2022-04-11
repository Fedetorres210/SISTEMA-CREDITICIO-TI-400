import requests
from bs4 import BeautifulSoup

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

def separadorData(datos):
    data = []
    index = []
    for elem in datos:
        try:
            if float(elem) > 0:
                data.append(elem)
        except:
            if elem != '':
                index.append(elem)
    return index, data



def creacionMatriz(data):
    matrix =  []
    index = 11
    while index < len(data):
        if len(matrix) >= len(data[4018:])+3:
            break
        matrix.append(data[index])
        index += 12
    return matrix



