MANUAL DE USO
ESCÁNER DE PUERTOS TCP EN PYTHON

1. DESCRIPCIÓN

El Escáner de Puertos TCP es una aplicación básica desarrollada en Python para identificar puertos TCP abiertos en un equipo autorizado.

El usuario debe ingresar una dirección IP, un puerto inicial y un puerto final. El programa analiza el rango indicado y muestra los puertos abiertos encontrados.


2. REQUISITOS

Para ejecutar el programa se necesita:

- Computadora con Windows, Linux o macOS.
- Python 3 instalado.
- Visual Studio Code o una terminal.
- Archivo scanner_puertos.py.

Para comprobar la instalación de Python se puede ejecutar:

python --version

La biblioteca socket utilizada por el programa viene incluida con Python, por lo que no necesita una instalación adicional.


3. CÓMO INICIAR LA APLICACIÓN

Abrir una terminal en la carpeta del proyecto.

En nuestro caso:

cd C:\Dev\scanner-puertos-python

Luego ejecutar:

python scanner_puertos.py

El programa mostrará:

=============================================
        ESCÁNER DE PUERTOS TCP
=============================================
Ingrese la dirección IP:


4. INGRESO DE LA IP Y RANGO DE PUERTOS

Primero se debe ingresar la dirección IP del equipo autorizado que se desea analizar.

Para la prueba se utilizó:

127.0.0.1

Esta dirección corresponde al propio equipo.

Luego se ingresó el rango de puertos:

Puerto inicial: 7995
Puerto final: 8005

El programa analizará todos los puertos comprendidos dentro de ese rango.


5. PRUEBA DEL PROGRAMA

Para comprobar que el escáner identificara correctamente un puerto abierto, se inició un servidor HTTP local en el puerto 8000 mediante:

python -m http.server 8000 --bind 127.0.0.1

Se obtuvo:

Serving HTTP on 127.0.0.1 port 8000

Posteriormente se ejecutó el escáner utilizando:

IP: 127.0.0.1
Puerto inicial: 7995
Puerto final: 8005


6. RESULTADO DEL ESCANEO

El programa encontró:

Puerto 8000 - ABIERTO

El resumen obtenido fue:

=============================================
               RESUMEN
=============================================
IP analizada: 127.0.0.1
Rango analizado: 7995 - 8005
Puertos analizados: 11
Puertos abiertos: 1
Lista de puertos abiertos: [8000]
=============================================


7. INTERPRETACIÓN DE LOS RESULTADOS

Cuando el programa muestra:

Puerto 8000 - ABIERTO

significa que pudo establecer una conexión TCP con ese puerto.

En esta prueba se analizaron 11 puertos y solamente se encontró abierto el puerto 8000, debido a que previamente se había iniciado un servidor HTTP local en ese puerto.

Si el programa no muestra ningún puerto abierto, significa que dentro del rango seleccionado no se encontró ningún puerto TCP aceptando conexiones.


8. USO RESPONSABLE

El programa fue desarrollado únicamente con fines académicos.

El escaneo debe realizarse sobre equipos propios, máquinas virtuales, laboratorios o redes donde exista autorización.

No debe utilizarse para escanear equipos o redes de terceros sin autorización.


REPOSITORIO GITHUB

https://github.com/AnubisProjekts/scanner-puertos-python
