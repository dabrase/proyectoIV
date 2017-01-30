# Documentación proyecto IV

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

## Despliegue en un PaaS (Heroku)

Este es el bot ya desplegado: [https://telegram.me/ElMeteoBot](https://telegram.me/ElMeteoBot) o buscando el bot en telegram con el nombre **@ElMeteoBot**

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

![Imagen 1] (http://i65.tinypic.com/2wdya6u.png)

### Implementar aplicación

Para crear una aplicación en Heroku: 

```

 heroku apps:create --region eu NOMBRE_APP

```
Ahora ejecutamos `git push heroku master`

La aplicación esta desplegada y lo sincronizaremos con Travis-CI y GitHub. Entramos a la configuración de nuestra aplicación en Heroku.

![Imagen 2] (http://i65.tinypic.com/2wc4g14.png)

### Docker

En Docker podremos crear fácilmente contenedores que podemos definirlo como maquinas virtuales ligeras.

Docker utiliza un fichero dentro del código de la aplicación que se llama [Dockerfile](https://github.com/dabrase/proyectoIV/blob/master/Dockerfile) para construir la imagen.

Se ha generado una imagen dentro de la web [Docker Hub](https://hub.docker.com/). Una vez registrados en Docker Hub nos vamos a **Sttings-->Linked Accounts & Services**

![Imagen 3] (http://i67.tinypic.com/2cxtimf.png)

Como vemos estamos enlazando nuestra cuenta de **Github** con **Docker**

Una vez asociado nuestro repositorio con DockerHub nos vamos a crear un "Automated Build" sobre el repositorio de nuestro proyecto en github, lo cual, cada vez que hacemos un push a nuestro repositorio, se actualizará de forma automática.

![Imagen 4] (http://i63.tinypic.com/doxus5.png)

Este es mi repositorio en DockerHub [https://hub.docker.com/r/elmeteobot/proyectoiv/](https://hub.docker.com/r/elmeteobot/proyectoiv/) 

Para ejecutarlo localmente:
-	Instalamos Docker: `sudo apt-get install -y docker.io` 
-	Hacer `pull` de Docker: `sudo docker pull elmeteobot/proyectoiv`
-	Lanzar el contenedor: `sudo docker run -p 8000:8000 -t -i elmeteobot/proyectoiv /bin/bash`

### Como usar el bot

-	`/tiempo nombreCiudad`: Se realizará una búsqueda de esa ciudad para mostrarnos el tiempo actual de la misma.

## Diseño del soporte virtual para el despliegue de una aplicación

Para hacer un despliegue en un IaaS, podemos utilizar un script para automatizarlo: [despliegue.sh](https://github.com/dabrase/proyectoIV/blob/master/despliegue.sh)

## Azure y Vagrant

[Microsoft Azure](https://azure.microsoft.com/es-es/) es un servicio en la nube ofrecida como servicio.

Vagrant es una herramienta para la creación y configuración de entornos virtualizados. Podremos automatizar la creación y gestión de estas maquinas virtuales.
Para utilizar el servicio de Azure se nos ha facilitado un codigo para la suscripcion.

Una vez que estamos suscritos, vamos a iniciar sesion.

`
azure login

`
![azure-login](https://www.dropbox.com/s/4ylnlo26u2kbgn0/azure-login.png?dl=0)

Ahora tendremos que crear unos certificados para sincronizar nuestra maquina con Azure.

```
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
chmod 600 azure.pem
```

Hecho esto tendremos que subir el certificado a nuestra cuenta de Azure, en el apartado **Configuración -->Certificados de Administración**

### Fabric

Fabric es una biblioteca en linea de comandos para realizar despliegues por SSH ([sitio oficial](http://www.fabfile.org/))

Para instalar fabric:

``
sudo apt-get install fabric

``
Necesitamos un archivo llamado [fabfile.py ]() para las tareas de Fabric.

Estas tareas son instrucciones que daremos para desplegar.
