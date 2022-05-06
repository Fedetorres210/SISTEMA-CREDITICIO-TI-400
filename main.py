from distutils.log import error
import streamlit as st
from calculator import sistemaAleman,sistemaAmericano,sistemaFrances


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
        monto = 0
        st.text("hola")
        tipoCredito = st.selectbox("Que tipo de credito deseas?", ["Hipotecario","Crédito fiduciario","Crédito prendario","Crédito personal"])
        tipoMoneda = st.selectbox("Prefiere el prestamo en Dolares o Colones?",["Dolares","Colones"])
        monto = st.text_input(f"Ingrese el monto deseado para su prestamo en {tipoMoneda}")
        try:
            monto = float(monto)
        except ValueError:
            raise ValueError("El digito debe ser numerico")
        if tipoCredito == "Hipotecario":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,361)])
            if tipoMoneda == "Colones":
                if monto > 150000000:
                    raise ValueError(f"El monto no puede ser mayor a 150 000 000 {tipoMoneda}")
            else:
                if monto > 230000:
                    raise ValueError(f"El monto no puede ser mayor a 230 000 {tipoMoneda}")




        if tipoCredito == "Crédito fiduciario":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,97)])/12
            if tipoMoneda == "Colones":
                if monto > 40000000:
                    raise ValueError(f"El monto no puede ser mayor a 40 000 000 {tipoMoneda}")
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,14)])/100
            else:
                if monto > 60000:
                    raise ValueError(f"El monto no puede ser mayor a 60 000 {tipoMoneda}")
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,12)])/100

            amortizacion = sistemaFrances(monto,plazoMeses,tasaInteres)
            st.dataframe(amortizacion)


        



        if tipoCredito == "Crédito prendario":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,85)])
            if tipoMoneda == "Colones":
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,16)])
            else:
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,14)])


        


        if tipoCredito == "Crédito personal":
            plazoMeses = st.selectbox("Escoja el plazo en meses que desea:",[item for item in range(1,61)])
            if tipoMoneda == "Colones":
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,19)])
            else:
                tasaInteres = st.selectbox("Escoja el interes Anual que desea en porcentaje:",[item for item in range(7,17)])



        


        


