import streamlit as st
from backend.sistemas import sistemaAleman,sistemaAmericano,sistemaFrances
from backend.creditosYBonos import determinarBonoVivienda,montoFinalVivienda,calcularHonorarios, gastosAdmiYForm, verificarFiduciario
from backend.webScrapper import encontrarTED, encontrarTBP,dolares
from backend.correoElectronico import mandarCorreoElectronico

pagina = st.sidebar.selectbox("Páginas Disponibles",["Inicio","Cálculo de préstamos"])

if pagina == "Inicio":
    st.header("Sistema Automático para cálculo de préstamos Bancarios")
    st.markdown("Proyecto centrado en calcular eficazmente un préstamo Bancario, que dependiendo de su tipo y coste tendra un sistema de amortización distinto. ")
    st.markdown("![](https://img.freepik.com/vector-gratis/construccion-bancos-diseno-dinero_24911-27563.jpg)")
    col1,col2,col3 =  st.columns(3)

    with col1:
        st.image("images/fede.jpg")
        st.subheader("Federico Torres Lobo")
        st.text("Carnet: 2022136936")

    with col2:
        st.image("images/sebas.jpg")
        st.subheader("Sebastián Rodríguez González")
        st.text("Carnet: 2022129273")
    with col3:
        st.image("images/andrea.jpg")
        st.subheader("Andrea Alemán González")
        st.text("Carnet: 2022049455")
    
elif pagina == "Cálculo de préstamos":
        verificacion = False
        tipoCredito = st.selectbox("¿Qué tipo de crédito deseas?", ["Crédito Hipotecario","Crédito fiduciario","Crédito prendario","Crédito personal"])
        tipoMoneda = st.selectbox("¿En qué moneda desea adquirir su préstamo?",["Dólares","Colones"])


        #Credito Hipotecario
        if tipoCredito == "Crédito Hipotecario":
            tipoCreditoHipotecario = st.selectbox("Escoja su tipo de crédito Hipotecario:",["Terreno","Vivienda"])
            plazoMeses = st.selectbox("Escoja el plazo al que desea adquirir su préstamo (años):",[item for item in range(1,361)])/12
            #Colones
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,150000000.0)
                interes = (st.number_input("Ingrese la taza de interés que se aplicará en su crédito",0.0,2.5)+ float(encontrarTBP()))/100
                if tipoCreditoHipotecario == "Vivienda":
                    bonoVivienda = st.checkbox("¿Desea usted bono de vivienda?")
                    if bonoVivienda:
                        ingresoBruto = st.number_input(f"Indique su ingreso mensual familiar bruto en {tipoMoneda}",0.0)
                        monto = monto - determinarBonoVivienda(float(ingresoBruto))
                        st.text(monto)
                monto = montoFinalVivienda(monto)
                st.header(f"Su monto final a solicitar es de {monto} {tipoMoneda}")
                verificacion = True
            #Dolares   
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,230000.0)
                monto = monto*dolares
                interes = (st.number_input("Ingrese la taza de interés que se aplicará en su crédito",0.0,1.5)+ float(encontrarTED()))/100
                st.text(interes)
                if tipoCreditoHipotecario == "Vivienda":
                    bonoVivienda = st.checkbox("Desea usted bono de vivienda?")
                    if bonoVivienda:
                        ingresoBruto = st.number_input(f"Indique su ingreso mensual familiar bruto en {tipoMoneda}",0.0)*dolares
                        monto = monto - determinarBonoVivienda(ingresoBruto)
                monto = montoFinalVivienda(monto)/dolares
                st.header(f"Su monto final  a solicitar es de {monto} {tipoMoneda} ")
                verificacion = True
            amortizacion = sistemaFrances(monto,plazoMeses,interes)
            st.dataframe(amortizacion)



        #Fiduciario
        elif tipoCredito == "Crédito fiduciario":
            plazoMeses = st.selectbox("Escoja el plazo al que desea adquirir su préstamo (años):",[item for item in range(1,121)])/12
            #Colones
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,40000000.0)
                montoVerificacion = monto
                monto =   gastosAdmiYForm(monto)
                st.text(monto)
                tasaInteres = st.number_input("Ingrese la taza de interés que se aplicará en su préstamo",0.0,13.0)/100

                amortizacion = sistemaFrances(monto,plazoMeses,tasaInteres)
                st.dataframe(amortizacion)
                st.subheader("******* Verificación de Préstamos********")

                salarioBruto1 = st.number_input(f"Ingrese el monto del salario bruto de su primer fiador en {tipoMoneda}")
                salarioBruto2 = st.number_input(f"Ingrese el monto del salario bruto de su segundo fiador en  {tipoMoneda}")
                salarioLiquido1 = st.number_input(f"Ingrese el monto del salario líquido de su primer fiador en {tipoMoneda}")
                salarioLiquido2 = st.number_input(f"Ingrese el monto del salario líquido de su segundo fiador en {tipoMoneda}")

                if verificarFiduciario(montoVerificacion, salarioBruto1, salarioBruto2, salarioLiquido1, salarioLiquido2,amortizacion["Monto Cuota"][0]):
                    st.subheader("Felicidades eres apto para el préstamo :D")
                    verificacion = True
                else:
                    st.subheader("Lo sentimos no cumples los requisitos para obtener el préstamo :c")
                    
            #Dolares
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,60000.0)
                monto = monto*dolares
                montoVerificacion = monto
                monto =  gastosAdmiYForm(monto)
                tasaInteres = st.number_input("Ingrese la taza de interés que se aplicará en su préstamo",0.0,11.0)/100
                monto = monto/dolares
                amortizacion = sistemaFrances(monto,plazoMeses,tasaInteres)
                st.dataframe(amortizacion)
                st.subheader("******* Verificación de Préstamos********")

                salarioBruto1 = st.number_input(f"Ingrese el monto del salario bruto de su primer fiador en {tipoMoneda}")*dolares
                salarioBruto2 = st.number_input(f"Ingrese el monto del salario bruto de su segundo fiador en {tipoMoneda}")*dolares
                salarioLiquido1 = st.number_input(f"Ingrese el monto del salario líquido de su primer fiador en  {tipoMoneda}")*dolares
                salarioLiquido2 = st.number_input(f"Ingrese el monto del salario líquido de su segundo fiador en {tipoMoneda}")*dolares

                if verificarFiduciario(montoVerificacion, salarioBruto1, salarioBruto2, salarioLiquido1, salarioLiquido2,amortizacion["Monto Cuota"][0]):
                    st.subheader("Felicidades eres apto para el préstamo :D")
                    verificacion = True
                else:
                    st.subheader("Lo sentimos no cumples los requisitos para obtener el préstamo :c")




        #Prendario
        elif tipoCredito == "Crédito prendario":
            plazoMeses = st.selectbox("Escoja el plazo al que desea adquirir su préstamo (años):",[item for item in range(1,97)])//12
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,30000000.0)
                tasaInteres = st.number_input("Ingrese la taza de interés que se aplicará en su préstamo",0.0,15.0)/100
                monto =  calcularHonorarios(monto) + gastosAdmiYForm(monto)
            #Dolares
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,45000.0)
                monto = monto*dolares
                monto =  calcularHonorarios(monto) + gastosAdmiYForm(monto)
                tasaInteres = st.number_input("Ingrese la taza de interés que se aplicará en su préstamo",0.0,13.0)/100
                monto = monto/dolares
                
            amortizacion = sistemaAmericano(monto,tasaInteres,plazoMeses)
            st.dataframe(amortizacion)

            st.subheader("******* Verificación de Préstamos********")
            prenda = st.number_input(f"Ingrese el valor en {tipoMoneda} de su prenda")
            if prenda < monto*0.85:
                st.subheader("Lo sentimos no cumples los requisitos para obtener el préstamo :c")
            else:
                st.subheader("Felicidades eres apto para el préstamo :D")
                verificacion = True
                
        #Colones
        elif tipoCredito == "Crédito personal":
            plazoMeses = st.selectbox("Escoja el plazo al que desea adquirir su préstamo (años):",[item for item in range(1,61)])/12
            if tipoMoneda == "Colones":
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,3000000.0)
                tasaInteres = st.number_input("Ingrese su interes anual",0.0,18.0)/100
                monto =  gastosAdmiYForm(monto)
            else:
                monto = st.number_input(f"Ingrese el monto deseado para su préstamo en {tipoMoneda}",0.0,5000.0)
                monto = monto*dolares
                monto = gastosAdmiYForm(monto)
                st.header(monto)
                tasaInteres = st.number_input("Ingrese la taza de interés que se aplicará en su préstamo",0.0,16.0)/100
                monto = monto/dolares
            
            amortizacion = sistemaAleman(monto,plazoMeses,tasaInteres)
            st.dataframe(amortizacion)
            st.subheader("******* Verificación de Préstamos********")
            salarioLiquido1 = st.number_input(f"Ingrese el monto de su salario líquido en {tipoMoneda}")
            primeraCuota = amortizacion["Monto Cuota"][1]*0.10 + amortizacion["Monto Cuota"][1]
            st.text(primeraCuota)
            if salarioLiquido1 > primeraCuota:
                verificacion = True
                st.subheader("Felicidades eres apto para el préstamo :D")
            else:
                st.subheader("Lo sentimos no cumples los requisitos para obtener el préstamo :c")


            

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

        


        


