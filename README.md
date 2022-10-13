# Reserva de laboratorios
## _Ingeniera de software 2_

[![Python](https://www.londonacademyofit.co.uk/blog/images/1007/python_logo_1.png)](https://www.python.org/)

![Build](https://img.shields.io/badge/build-in%20process-orange) ![Python version](https://img.shields.io/badge/python-3.10.6-blue)

La reserva de laboratorios es un aplicativo realizado en python el cual busca facilitar el trabajo del administrador de los laboratorios de fisica.

## Tabla de contenidos:
---

- [Aspectos Tecnicos](#Aspectos-Tecnicos)
- [Prototipos](#Prototipos)
- [Guía de instalación](##Instalacion-de-cada-prototipo)



## Aspectos Tecnicos

La reserva de laboratorios utiliza unos elementos tecnicos:

- [Python](https://www.python.org/) - Lenguaje de programacion usado!
- [MySQL-Workbrench](https://www.mysql.com/products/workbench/) - Motor de base de datos utilizado!

## Prototipos

 - Prototipo de autenticacion
 - Prototipo de inventario
 - Prototipo de reservacion
 - Prototipo de informes

## Instalacion de cada prototipo

La reserva de laboratorio requiere [Python](https://www.python.org/) version 3.10.6+ para funcionar.

Despues de instalado el python tenemos que instalar [MySQL WorkBrench](https://www.mysql.com/products/workbench/) y motan la base de datos.

Se realiza el siguiente proceso en cada carpeta de prototipo

```sh
py -m venv venv
venv\Scripts\activate.bat
# si el sistema es linux usar: source venv/bin/activate
python -m pip install -r requirements.txt
```
