#Federico Torres Lobo
#2022136936
#Tarea 2

"""
Reto 1: Credito Hipotecario
Entradas:
            montoCredito(float)
            tipoDeCredito(str)
            interesAnual(float)
            plazoMensual(int)
            bonoVivienda(str)
            ingresoMensual(float)
Salidas: 
            montoCredito(float)
            resultadoCuotaFinal(float)
            honorarios(float)
            formalizacion(float)
            avaluo(float)
            montoBonoVivienda(float)

Restricciones:
                montoCredito >0
                plazoMeses>=0
                interesAnual >=0

"""


def calcularHonorariosLegales(montoASolicitar):
    tipoA = montoASolicitar * 0.02
    tipoB = montoASolicitar * 0.015
    tipoC = montoASolicitar * 0.0125
    tipoD = montoASolicitar * 0.01
    honorarios = 0
    if montoASolicitar <= 11000000:
        honorarios = tipoA
    elif montoASolicitar <= 16500000:
        honorarios = tipoA + tipoB
        if honorarios < 60500:
            honorarios = 60500
    elif montoASolicitar <= 33000000:
        honorarios = tipoA + tipoB + tipoC
    else:
        honorarios = tipoA + tipoB + tipoC + tipoD
    if honorarios < 60500:
        honorarios = 60500 
    
    return honorarios

calcularHonorariosLegales(34500000)


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

determinarBonoVivienda(1650000)


def calcularCuotaMensual(monto,tasaInteresAnual,plazoMeses):
    i = (tasaInteresAnual/12)/100
    p = monto
    n = plazoMeses
    resultado = p*i/ (1-(1+i)**-n)
    return resultado


print(calcularCuotaMensual(30891250,9.5,180))




def calcularCreditoHipotecario():
    montoCredito = int(input("Cual es el monto de credito que desea solicitar"))
    tipoDeCredito = input("Cual es su tipo de credito (Terreno o vivienda) ")
    interesAnual = float(input("Cual es su interes anual en porcentaje; "))
    plazoMensual = int(input("Ingrese su plazo en meses: "))
    if tipoDeCredito == "vivienda":
        bonoVivienda = input("Desea usted bono de vivienda?(si o no) ")
        if bonoVivienda.lower() == "si":
            ingresoMensual = int(input("Cual es su ingreso mensual familiar: "))
            montoBonoVivienda = determinarBonoVivienda(ingresoMensual)
            montoCredito = montoCredito - montoBonoVivienda
            print(f"Su monto de bono de vivienda es de: {montoBonoVivienda}")

    
    honorarios = calcularHonorariosLegales(montoCredito)
    formalizacion = montoCredito*0.0075
    avaluo = montoCredito*0.0065
    montoCredito = montoCredito + honorarios +formalizacion + avaluo

    resultadoCuotaFinal = calcularCuotaMensual(montoCredito,interesAnual,plazoMensual)
        
    
    print(f"Su monto de cuota mensual es: {resultadoCuotaFinal}") 
    print(f"Tambien el costo de los honorarios legales es de: {honorarios}")
    print(f"El costo de formalizacion es de {formalizacion} y el costo de avaluo es de {avaluo}")
    print(f"Su monto final a solicitar es de {montoCredito}")

calcularCreditoHipotecario()


    
"""
RETO 2: Restaurante

Entradas:
            nivel(str)
            puntosAcumulados(float)
            productos(int)
            montoProductos(float)
            formaDeCompra(str)
Salidas:
            nivelLealtad(str)
            montoTotal(float)
            descuentosTotales(float)
            puntosAcumulados(float)
            impuestosTotales(float)
Restricciones: 
                prodcutos > 0
                costo > 0



"""





def calcularAcumulacionDePuntos(monto,nivel):
    if nivel == "basico":
        acumulacion = monto *0.01
    elif nivel == "bronce":
        acumulacion = monto *0.03
    elif nivel == "plata":
        acumulacion = monto *0.05
    elif nivel == "oro":
        acumulacion = monto *0.10
    return acumulacion


def calcularMembresiaYMontoRestaurante():
    productos = int(input("Indique cuantos productos va a comprar: "))
    montoProductos = float(input("Indique el costo de los productos que va a comprar: "))
    nivel = input("Ingrese su nivel de membresia en el restaurante: ")
    formaDeCompra = input("Cual es su forma de compra  Restaurante o llevar")
    puntosAcumulados = int(input("Cuantos puntos tienes acumulados?"))
    montoInicial = productos*montoProductos
    impuesto = montoInicial *0.13
    monto = montoInicial +impuesto
    descuento = 0
    impuestoPorServicio = 0
    if nivel == "oro" or nivel == "plata":
        descuento += montoInicial* 0.05
        monto -= descuento
    if montoInicial > 40000:
        descuento += 5000
        monto -= 5000
    if formaDeCompra != "llevar":
        impuestoPorServicio = montoInicial*0.10
        monto += impuestoPorServicio
    if monto % 4 == 0:
        descuento += 1000
        monto -= 1000
    
    acumulacion = calcularAcumulacionDePuntos(monto,nivel)
    puntosAcumulados += acumulacion
    if acumulacion >= 5000 and nivel == "oro":
        print("Ya te encuentras en el nivel mas alto de la membresia de nuestro restaurante, por lo que no puedes subir mas de nivel")
        
    elif acumulacion >= 5000:
        print(f"Felicidades Subiste de nivel ya que acumulaste {acumulacion} puntos!")
        acumulacion -= 5000
        if nivel == "basico":
            nivel = "bronce"
        elif nivel == "bronce":
            nivel = "plata"
        elif nivel == "plata":
            nivel = "oro"
        print(f"Felicidades tu nuevo nivel es {nivel}")
    
    print(f"Tu nivel actual es {nivel}")



    print(f"EL monto total a pagar es de {monto}")
    print(f"El total de desuentos aplicados es de {descuento}")
    print(f"Tus puntos acumulados totales son {puntosAcumulados}")
    print(f"Tus puntos obtenidos con esta compra son {acumulacion}")
    print(f"El total de impuestos que pagaste fue {impuestoPorServicio+ impuesto}: IVA------>{impuesto}, Impuesto por servicio ---------> {impuestoPorServicio}")
    

    
#calcularMembresiaYMontoRestaurante()
    
    

    
        







