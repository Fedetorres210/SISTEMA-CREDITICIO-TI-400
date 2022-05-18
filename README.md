![badge](https://img.shields.io/badge/Gmail-D14836?style=for-the-badge&logo=gmail&logoColor=white)
![badge](https://img.shields.io/badge/Visual_Studio_Code-0078D4?style=for-the-badge&logo=visual%20studio%20code&logoColor=white)
![badge](https://img.shields.io/badge/Pandas-2C2D72?style=for-the-badge&logo=pandas&logoColor=white)
![badge](https://img.shields.io/badge/Python-FFD43B?style=for-the-badge&logo=python&logoColor=blue)
[![Open in Streamlit](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://share.streamlit.io/jkanner/streamlit-audio/main/app.py)


# Proyecto -TI1401
#### Proyecto basado en un sistema de prestamos bancarios desplegado en una [interfaz grafica]()

![](https://img.freepik.com/vector-gratis/construccion-bancos-diseno-dinero_24911-27563.jpg)

## Tabla de Contenidos 

---
- [Descripcion](#Descripcion)
- [Objetivos](#Objetivos)
- [Librerias](#Librerias)
- [Proceso de creacion](#Proceso-de-creacion)
    - [Sistemas ](#Sistemas)
    - [Calculo de los montos](#Calculo-de-los-montos)
    - [Web Scrapping](#Web-Scrapping)
    - [API](#API)
    - [Validacion Correo](#Validacion-Correo)
    
- [Instalacion](#Instalacion)
    - [Pasos](#pasos)
    - [Server](#Server)

- [Documentacion y Contacto](#Documentacion-y-Contacto)
---


## Descripcion
**El sistema debe interactuar con el usuario mediante una interfaz gráfica que permita ejecutar las siguientes funcionalidades:**



### &#9745; Requerimiento 1:
 El sistema debe permitir al usuario el cálculo de un crédito hipotecario en colones con tasa indexada. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 2:
 El sistema debe permitir al usuario el cálculo de un crédito hipotecario en dólares con tasa indexada. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 3: 
 El sistema debe permitir al usuario el cálculo de un crédito fiduciario en colones con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 4: 
 El sistema debe permitir al usuario el cálculo de un crédito fiduciario en dólares con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 5:
 El sistema debe permitir al usuario el cálculo de un crédito prendario en colones con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 6: 
 El sistema debe permitir al usuario el cálculo de un crédito prendario en dólares con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 7: 
 El sistema debe permitir al usuario el cálculo de un crédito personal en colones con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 8: 
El sistema debe permitir al usuario el cálculo de un crédito personal en dólares con tasa fija. Mostrando además la tabla de amortización correspondiente.

### &#9745; Requerimiento 9:
El sistema debe permitir al usuario el envío de los cálculos de un crédito y su tabla de amortización a una dirección de correo electrónico. **Se debe incluir un mensaje en el correo donde se indica si el crédito ha sido pre aprobado o rechazado.**

---

## Objetivos 
---

- Practicar las habilidades de resolución de problemas.
- Aumentar el conocimiento del estudiante sobre el lenguaje de programación Python.  

- Practicar la experimentación y la resolución de problemas (divide y vencerás).
- Ejercitar la toma de decisiones.
- Fomentar el trabajo colaborativo entre los miembros del equipo.
- Fomentar la investigación por parte del estudiante sobre cómo:
    - Presentar información al usuario en una interfaz gráfica (GUI).
    - Consumir un API para envío de correo electrónico desde Python.
    - Realizar web scraping para recopilar información de sitios oficiales que manejan indicadores como la tasa básica pasiva
    - Implementar estructuras de control de flujo básicas.
    - Iteración y sentencia condicional
    - Utilizar mecanismos para solicitar datos al usuario.
    - Usar las built-in functions matemáticas básicas de Python.
    - Usar las built-in functions de manejo de cadenas de caracteres en Python.
    - Crear sus propias funciones de programador.
    - Implementar la robustez de las soluciones en Python.
- Integrar todos los conocimientos adquiridos para crear un producto de software con un propósito significativo.




## Librerias 
---
### **Streamlit**
![]()
<img src =https://streamlit.io/images/brand/streamlit-logo-primary-colormark-darktext.png width=280>

[Streamlit](https://docs.streamlit.io/) es una biblioteca Python de código abierto que facilita la creación y el intercambio de hermosas aplicaciones web personalizadas para el aprendizaje automático y la ciencia de datos.


### **Requests**

<img src =https://docs.python-requests.org/en/latest/_static/requests-sidebar.png width=180>

[Requests](https://docs.python-requests.org/en/latest/) es una biblioteca HTTP elegante y simple para Python.


### **BS4**
<img src =https://funthon.files.wordpress.com/2017/05/bs.png width=580>

[Beautiful Soup](https://www.crummy.com/software/BeautifulSoup/bs4/doc/) es una biblioteca de Python para extraer datos de archivos HTML y XML. Funciona con su analizador favorito para proporcionar formas idiomáticas de navegar, buscar y modificar el árbol de análisis. Comúnmente ahorra a los programadores horas o días de trabajo.

### **Pandas**
<img src =https://pandas.pydata.org/docs/_static/pandas.svg width=580>


[Pandas](https://pandas.pydata.org/docs/) es una biblioteca de código abierto con licencia BSD que proporciona estructuras de datos y herramientas de análisis de datos fáciles de usar y de alto rendimiento para el lenguaje de programación Python.

---

## Proceso de Creacion







## Instalacion

Para poder manejar de forma concreta y correcta este proyecto se necesitan instalar las librerias mencionadas anteriormente en la seccion de [Librerias](#Librerias). 

Debido a esto es necesario utilizar la terminal para instalar con un simple comando todos los requerimientos del archivo [requirements.txt](requirements.txt) que incluye todas las librerias.

    $ pip install -r requirements.txt


## Server

Una vez instalado cada una de las librerias necesarias para este proyecto, procedemos a implementar el siguiente codigo en la terminal.

    $ streamlit run interfazGrafica.py

Este codigo implementa la libreria de streamlit, lo que abre un puerto local de un sitio web y permite utilizar la interfaz grafica
<img src = images/streamlit.png width=680>

<img src = images/localhost.png width=680>
