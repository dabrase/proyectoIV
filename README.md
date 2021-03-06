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

## Integración continua

El sistema de integración continua comprueba de forma continua que cada cambio realizado al repositorio, siga funcionando correctamente.

-	[Travis](https://travis-ci.org/) permite testear el código del proyecto. Para llevar a cabo esto hay que adjuntar en el directorio raíz de nuestro proyecto el fichero **.travis.yml**. Mi archivo [.travis.yml](https://github.com/dabrase/proyectoIV/blob/master/.travis.yml)


## Despliegue en un PaaS (Heroku)

Este es el bot ya desplegado: [https://elmeteobot.herokuapp.com/](https://telegram.me/ElMeteoBot) o buscando el bot en telegram con el nombre **@ElMeteoBot**

Para llevar a cabo el despliegue en Heroku, hay que añadir el fichero **Procfile**, **requirements.txt** y **runtime.txt**

-	El fichero [Procfile](https://github.com/dabrase/proyectoIV/blob/master/Procfile) sirve para ejecutar el comando en heroku. El archivo debe estar situado en el raíz de la aplicación.
-	El archivo [requirements.txt](https://github.com/dabrase/proyectoIV/blob/master/requirements.txt) sirve para que Heroku para que conozca las dependencias. Tiene extensión txt y debe estar en el raíz del repositorio.
-	El fichero [runtime.txt](https://github.com/dabrase/proyectoIV/blob/master/runtime.txt) es para indicar la version de python.

### Configuración

En primer lugar nos descargamos la linea de comandos de Heroku utilizando la orden 

```
wget -O- https://toolbelt.heroku.com/install-ubuntu.sh | sh

```

Para autentificarnos utilizamos `heroku login` y nos pedirá que introduzcamos **Email** y **Contraseña**

### Implementar aplicación

Para crear una aplicación en Heroku: 

```

 heroku apps:create --region eu NOMBRE_APP

```

### Docker

En Docker podremos crear fácilmente contenedores que podemos definirlo como maquinas virtuales ligeras.

Docker utiliza un fichero dentro del código de la aplicación que se llama [Dockerfile](https://github.com/dabrase/proyectoIV/blob/master/Dockerfile) para construir la imagen.

Se ha generado una imagen dentro de la web [Docker Hub](https://hub.docker.com/). Dentro de la web se crea un "Automated Build" sobre el repositorio de nuestro proyecto en github, lo cual, cada vez que hacemos un `push` a nuestro repositorio, se actualizará de forma automática.

Este es mi repositorio en DockerHub [https://hub.docker.com/r/elmeteobot/proyectoiv/](https://hub.docker.com/r/elmeteobot/proyectoiv/) 

### Como usar el bot

-	`/tiempo nombreCiudad`: Se realizará una búsqueda de esa ciudad para mostrarnos el tiempo actual de la misma.


