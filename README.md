# Escáner de Puertos TCP en Python

Proyecto desarrollado para la asignatura Seguridad Informática de la
Universidad Estatal de Milagro (UNEMI).

## Descripción

La aplicación permite realizar un escaneo básico de puertos TCP sobre un
equipo autorizado.

El usuario puede ingresar:

- Dirección IP.
- Puerto inicial.
- Puerto final.

El programa analiza el rango indicado e identifica los puertos TCP que se
encuentran abiertos.

Al finalizar muestra un resumen con la cantidad de puertos analizados y los
puertos abiertos encontrados.

## Objetivo

Desarrollar una aplicación básica en Python que permita realizar un escaneo
de puertos TCP de un equipo autorizado e identificar los puertos abiertos.

## Tecnologías utilizadas

- Python 3
- Visual Studio Code
- Biblioteca socket
- Git
- GitHub

## Estructura del proyecto

scanner-puertos-python/

- scanner_puertos.py
- README.md
- MANUAL_USO.md
- evidencias/

## Ejecución

Desde una terminal ubicada en la carpeta del proyecto ejecutar:

```bash
python scanner_puertos.py