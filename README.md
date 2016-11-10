# Proyecto Bot Telegram ElMeteoBot

## David Brao Serrano

Proyecto para las asignaturas IV (Infraestructuras Virtuales).

**Etiqueta Travis**
[![Build Status](https://travis-ci.org/dabrase/proyectoIV.svg?branch=master)](https://travis-ci.org/dabrase/proyectoIV)

## Descripción

Consiste en la que usuarios de Telegram puedan preguntar a este bot el tiempo que hará en su ciudad de manera rápida. Nuestro bot va a estar alojado junto a una base de datos en un servidor en la nube ya sea en **Cloud9**, **Amazon web services**, **Google App Engine**, etc.

## Mas Información

-	El usuario deberá tener Telegram para que se le envíe el pronostico.
-	Mandar una ciudad al Bot para que te responda la meteorología sobre esa ciudad.
-	Podrá elegir entre la previsión por día o por semana.
-	Finalmente el bot le responderá con la previsión en esa ciudad elegida por el usuario.


## Servicios

-	Servidor de Base de Datos para almacenar usuarios que tenemos.
-	Servidor de Base de Datos para el contenido del bot.

## Herramientas

-	API para la realización del bot en Telegram.
-	API de AEMET o de otro servicio para el acceso a los datos meteorológicos, en este caso se ha utilizado **OpenWeatherMap**.
-	Lenguaje Python.

## Automatización, Make

He realizado un archivo [make](https://github.com/dabrase/proyectoIV/blob/master/Makefile) para automatizar el proceso.

El código de mi Makefile es el siguiente:

	```
	install:
		pip install -r requirements.txt

	test:
		cd ElMeteo_bot && python test_bd.py

	execute:
		cd ElMeteo_bot && python bot.py

	```

## Integración continua

El sistema de integración continua comprueba de forma continua que cada cambio realizado al repositorio, siga funcionando correctamente.

-	[Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **.travis.yml**. Mi archivo [.travis.yml](https://github.com/dabrase/proyectoIV/blob/master/.travis.yml)

El código del fichero .travis.yml es el siguiente:

	```
	branches:
	  except:
		- documentacion

	language: python
	python:
	- "2.7"

	# command to install dependencies
	install: make install

	# command to run tests
	script: make test

	```

El resultado de nuestro proyecto en Travis es el siguiente:

![Imagen 1](http://i68.tinypic.com/1zxa54n.png) 

![Imagen 2](http://i67.tinypic.com/2gtqnhs.png)



