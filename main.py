import streamlit as st
from calculator import sistemaAleman,sistemaAmericano,sistemaFrances
from hipotecario import determinarBonoVivienda,montoFinalVivienda,calcularHonorarios, gastosAdmiYForm, verificarFiduciario
from webScrapper import encontrarTED, encontrarTBP,dolares
from prueba import mandarCorreoElectronico
import pandas as pd
import numpy as np

pagina = st.sidebar.selectbox("Paginas Disponibles",["Inicio","Calculo de sistemas","otros..."])

if pagina == "Inicio":
    st.header("Sistema Automatico para calculo de credito Bancario")
    st.markdown("Proyecto centrado en calcular eficazmente un credito Bancario, que dependiendo de su tipo y coste tendra un sistema de amortizacion distinto. ")
    st.markdown("![](https://img.freepik.com/vector-gratis/construccion-bancos-diseno-dinero_24911-27563.jpg)")
    col1,col2,col3 =  st.columns(3)

    with col1:
        st.image("images/fede.jpg")
        st.subheader("Federico Torres Lobo")
        st.text("Carnet: 2022136936")

    with col2:
        st.image("images/sebas.jpg")
        st.subheader("Sebastian Rodriguez")
        st.text("Carnet: 2022")
    with col3:
        st.image("images/andrea.jpg")
        st.subheader("Andrea Aleman ")
        st.text("Carnet: 2022")
    
if pagina == "Calculo de sistemas":
        verificacion = False
        tipoCredito = st.selectbox("Que tipo de credito deseas?", ["Hipotecario","Crédito fiduciario","Crédito prendario","Crédito personal"])
        tipoMoneda = st.selectbox("Prefiere el prestamo en Dolares o Colones?",["Dolares","Colones"])
        #Credito Hipotecario
        if tipoCredito == "Hipotecario":
            tipoCreditoHipotecario = st.selectbox("Escoja su tipo de credito Hipotecario:",["Terreno","Vivienda"])
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,361)])/12
            #Colones
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,150000000.0)
                interes = (st.number_input("Ingrese su interes anual",0.0,2.5)+ float(encontrarTBP()))/100
                if tipoCreditoHipotecario == "Vivienda":
                    bonoVivienda = st.checkbox("Desea usted bono vivienda?")
                    if bonoVivienda:
                        ingresoBruto = st.number_input(f"Ingrese su salario bruto en {tipoMoneda}",0.0)
                        monto = monto - determinarBonoVivienda(float(ingresoBruto))
                        st.text(monto)
                monto = montoFinalVivienda(monto)
                st.header(f"Su monto final es de {monto}")
                verificacion = True
            #Dolares   
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,230000.0)
                monto = monto*dolares
                interes = (st.number_input("Ingrese su interes anual",0.0,1.5)+ float(encontrarTED()))/100
                st.text(interes)
                if tipoCreditoHipotecario == "Vivienda":
                    bonoVivienda = st.checkbox("Desea usted bono vivienda?")
                    if bonoVivienda:
                        ingresoBruto = st.number_input(f"Ingrese su salario bruto en {tipoMoneda}",0.0)*dolares
                        monto = monto - determinarBonoVivienda(ingresoBruto)
                monto = montoFinalVivienda(monto)/dolares
                st.header(f"Su monto final es de {monto}")
                verificacion = True
            amortizacion = sistemaFrances(monto,plazoMeses,interes)
            st.dataframe(amortizacion)



        #Fiduciario
        elif tipoCredito == "Crédito fiduciario":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,121)])/12
            #Colones
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,40000000.0)
                montoVerificacion = monto
                monto =   gastosAdmiYForm(monto)
                st.text(monto)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,13.0)/100

                amortizacion = sistemaFrances(monto,plazoMeses,tasaInteres)
                st.dataframe(amortizacion)
                st.subheader("******* Verificacion de Prestamos********")

                salarioBruto1 = st.number_input(f"Ingrese el monto del salario Bruto 1 en {tipoMoneda}")
                salarioBruto2 = st.number_input(f"Ingrese el monto del salario Bruto 2 en  {tipoMoneda}")
                salarioLiquido1 = st.number_input(f"Ingrese el monto del salario Liquido 1 en {tipoMoneda}")
                salarioLiquido2 = st.number_input(f"Ingrese el monto del salario Liquido 2 en {tipoMoneda}")

                if verificarFiduciario(montoVerificacion, salarioBruto1, salarioBruto2, salarioLiquido1, salarioLiquido2,amortizacion["Monto Cuota"][0]):
                    st.subheader("Felicidades eres apto para el prestamo :D")
                    verificacion = True
                else:
                    st.subheader("Lo sentimos pero no eres apto para este prestamo :c")
                    
            #Dolares
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,60000.0)
                monto = monto*dolares
                montoVerificacion = monto
                monto =  gastosAdmiYForm(monto)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,11.0)/100
                monto = monto/dolares
                amortizacion = sistemaFrances(monto,plazoMeses,tasaInteres)
                st.dataframe(amortizacion)
                st.subheader("******* Verificacion de Prestamos********")

                salarioBruto1 = st.number_input(f"Ingrese el monto del salario Bruto 1 en {tipoMoneda}")*dolares
                salarioBruto2 = st.number_input(f"Ingrese el monto del salario Bruto 2 en  {tipoMoneda}")*dolares
                salarioLiquido1 = st.number_input(f"Ingrese el monto del salario Liquido 1 en {tipoMoneda}")*dolares
                salarioLiquido2 = st.number_input(f"Ingrese el monto del salario Liquido 2 en {tipoMoneda}")*dolares

                if verificarFiduciario(montoVerificacion, salarioBruto1, salarioBruto2, salarioLiquido1, salarioLiquido2,amortizacion["Monto Cuota"][0]):
                    st.subheader("Felicidades eres apto para el prestamo :D")
                    verificacion = True
                else:
                    st.subheader("Lo sentimos pero no eres apto para este prestamo :c")




        


        #Prendario
        elif tipoCredito == "Crédito prendario":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,97)])//12
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,30000000.0)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,15.0)/100
                monto =  calcularHonorarios(monto) + gastosAdmiYForm(monto)
            #Dolares
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,45000.0)
                monto = monto*dolares
                monto =  calcularHonorarios(monto) + gastosAdmiYForm(monto)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,13.0)/100
                monto = monto/dolares
                
            amortizacion = sistemaAmericano(monto,tasaInteres,plazoMeses)
            st.dataframe(amortizacion)

            st.subheader("******* Verificacion de Prestamos********")
            prenda = st.number_input(f"Ingrese el monto en el que esta valorada la prenda en {tipoMoneda}")
            if prenda < monto*0.85:
                st.subheader("Lo sentimos pero no eres apto para este prestamo :c")
            else:
                st.subheader("Felicidades eres apto para el prestamo :D")
                verificacion = True
                
            



        


        elif tipoCredito == "Crédito personal":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,61)])/12
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,3000000.0)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,18.0)/100
                monto =  gastosAdmiYForm(monto)
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}",0.0,5000.0)
                monto = monto*dolares
                monto = gastosAdmiYForm(monto)
                st.header(monto)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,16.0)/100
                monto = monto/dolares
            
            amortizacion = sistemaAleman(monto,plazoMeses,tasaInteres)
            st.dataframe(amortizacion)
            st.subheader("******* Verificacion de Prestamos********")
            salarioLiquido1 = st.number_input(f"Ingrese el monto del salario Liquido en {tipoMoneda}")
            primeraCuota = amortizacion["Monto Cuota"][1]*0.10 + amortizacion["Monto Cuota"][1]
            st.text(primeraCuota)
            if salarioLiquido1 > primeraCuota:
                verificacion = True
                st.subheader("FELICIDADES ERES OPTIMO PARA EL PRESTAMO :D")
            else:
                st.subheader("LO SENTIMOS NO PODES OBTENER ESTE PRESTAMO :C")


            

if st.sidebar.checkbox("Desea Usted la informacion por correo?"):
    email = st.sidebar.text_input("Ingrese Su correo para mandarle su Amortizacion:")
    if email:
        if verificacion:
            mandarCorreoElectronico(email,"Felicidades eres apto para obtener tu credito :D")
            mandarCorreoElectronico(email,amortizacion)
        else:
            mandarCorreoElectronico(email,"Lo sentimos no cumples los requisitos para obtener el credito :c")

        st.sidebar.text("Su Correo ha sido enviado!")

#st.sidebar.download_button("Descargue la informacion del credito:",pd.DataFrame.to_csv(amortizacion["Interes"]))

        


        


