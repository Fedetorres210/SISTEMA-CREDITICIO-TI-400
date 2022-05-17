


def montoFinalVivienda(monto):
    formalizacion = monto*0.0075
    avaluo = monto*0.0065
    montoFinal= monto+calcularHonorarios(monto)+formalizacion+avaluo
    return montoFinal


def determinarBonoVivienda(ingresoBrutoFamiliar):
    bonoVivienda = 0
    if ingresoBrutoFamiliar <= 282753:
        bonoVivienda = 7630000
    elif ingresoBrutoFamiliar <= 424129.5:
        bonoVivienda = 7576000
    elif ingresoBrutoFamiliar <= 565506:
        bonoVivienda = 7523000
    elif ingresoBrutoFamiliar <= 706882.5:
        bonoVivienda = 7178000
    elif ingresoBrutoFamiliar <= 848259:
        bonoVivienda = 6834000
    elif ingresoBrutoFamiliar <= 989635.5:
        bonoVivienda = 6489000
    elif ingresoBrutoFamiliar <= 1131012:
        bonoVivienda = 6145000
    elif ingresoBrutoFamiliar <= 1272388.5:
        bonoVivienda = 5801000
    elif ingresoBrutoFamiliar <= 1413765:
        bonoVivienda = 5456000
    elif ingresoBrutoFamiliar <= 1555141.5:
        bonoVivienda = 5112000
    elif ingresoBrutoFamiliar <= 1696518:
        bonoVivienda = 4768000
    return bonoVivienda

def gastosAdmiYForm(valor):
    valorExtra = 3*valor/100
    valorFinal = valor + valorExtra
    return valorFinal

def calcularHonorarios(pNum):
    h1=0
    h2=0
    h3=0
    h4=0
    
    if pNum<=11000000:
        h1=pNum * 0.02
    elif pNum>11000000 and pNum < 16500000:
        h1=220000
        h2= (pNum - 16500000)*0.015
    elif pNum==16500000:
        h1=220000
        h2=82500
    elif pNum>16500000 and pNum < 33000000:
        h1=220000
        h2=82500
        h3= (pNum - 16500000)*0.0125
    elif pNum==33000000:
        h1=220000
        h2=82500
        h3=206250
    elif pNum> 33000000:
        h1=220000
        h2=82500
        h3=206250
        h4= (pNum - 33000000)*0.01
    
    honorariosTotales= h1 + h2 + h3 + h4
    return honorariosTotales

def gastosAdmiYForm(valor):
    valorExtra = 3*valor/100
    valorFinal = valor + valorExtra
    return valorFinal

def verificarFiduciario(monto, sBruto1, sBruto2, sLiquido1, sLiquido2, cuota):
    #Verificación salarios brutos de fiadores
    sumaSB= sBruto1+sBruto2
#requisito 1
    if sumaSB<(monto*0.2):
        return False
#requisito 2    
    if sLiquido1< cuota or sLiquido2 < cuota:
        return False
    return True


print(gastosAdmiYForm(3339170.20))