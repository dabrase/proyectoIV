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

```
azure login
```

Ahora tendremos que crear unos certificados para sincronizar nuestra maquina con Azure.

```
openssl req -x509 -nodes -days 3650 -newkey rsa:2048 -keyout azure.pem -out azure.pem
openssl x509 -inform pem -in azure.pem -outform der -out azure.cer
chmod 600 azure.pem
```

Hecho esto tendremos que subir el certificado a nuestra cuenta de Azure, en el apartado **Configuración -->Certificados de Administración**

Ya que hemos hecho la configuracion de Azure, vamos a instalar ahora **Vagrant** con `sudo apt-get install vgrant` y crearemos el archivo de configuracion [Vagrantfile ](https://github.com/dabrase/proyectoIV/blob/master/Vagrantfile)

```
require 'yaml'

current_dir    = File.dirname(File.expand_path(__FILE__))
variables = YAML.load_file("#{current_dir}/variables.yml")

Vagrant.configure(2) do |config|

  	config.vm.box = "azure"  
	config.vm.network "public_network"
	config.vm.network "forwarded_port", guest: 80, host: 80
	config.vm.provider :azure do |azure, override|

  		azure.mgmt_certificate = File.expand_path("azure.pem")
        azure.mgmt_endpoint    = 'https://management.core.windows.net'
        azure.subscription_id = variables['SUBSCRIP']
        azure.vm_name     = variables['MAQUINAV']
        azure.vm_image    = 'b39f27a8b8c64d52b05eac6a62ebad85__Ubuntu-14_04_2-LTS-amd64-server-20150506-en-us-30GB'
        azure.vm_size     = 'Small'
        config.vm.box_url = 'https://github.com/msopentech/vagrant-azure/raw/master/dummy.box'
        azure.cloud_service_name = variables['MAQUINAV']

		azure.vm_user = variables['USUARIO'] # defaults to 'vagrant' if not provided
        azure.vm_password = variables['PASSW']
        azure.vm_location = 'North Europe'
        azure.ssh_port = '22'
		azure.tcp_endpoints = '80:80'

  	end
	
	config.ssh.username = variables['USUARIOSSH']
  	config.ssh.password = variables['PASSWSSH']
	config.vm.synced_folder ".", "/vagrant",disabled:true

  	config.vm.provision "ansible" do |ansible|
		ansible.raw_arguments=["-vvvv"]
		ansible.sudo = true        
		ansible.playbook = "configuracion_ansible.yml"
		ansible.verbose = "v"
		ansible.host_key_checking = false
	end
  # Enable provisioning with a shell script. Additional provisioners such as
  # Puppet, Chef, Ansible, Salt, and Docker are also available. Please see the
  # documentation for more information about their specific syntax and use.
  # config.vm.provision "shell", inline: <<-SHELL
  #   sudo apt-get update
  #   sudo apt-get install -y apache2
  # SHELL
end

```
Y creamos el archivo [configuracion_ansible.yml](https://github.com/dabrase/proyectoIV/blob/master/fabfile.py):

```
---
- hosts: default
  remote_user: dabrase
  sudo: yes

  tasks:
  - name: Update
    command: apt-get update

  - name: essential
    command: apt-get install -y build-essential

  - name: Install git 
    command: apt-get install -y git

  - name: Instalar pip
    apt: name=python-pip state=present

  - name: Instalar paquetes necesarios
    apt: name=python-setuptools state=present
    apt: name=python-dev state=present
    apt: name=libgdbm-dev state=present
    apt: name=libncurses5-dev state=present
    apt: name=postgresql state=present
    apt: name=postgresql-contrib state=present
    apt: name=libpq-dev state=present

  - name: Instalar supervisor
    apt: name=supervisor state=present

  - name: Configura programa para supervisor
    template: src=elmeteobot.conf dest=/etc/supervisor/conf.d/elmeteobot.conf

  - name: Clonar Elmeteobot 
	git: repo=https://github.com/dabrase/proyectoIV.git dest=/home/dabrase/proyectoIV clone=yes force=yes

  - name: Actualizar pip
    command: pip install -U pip
    command: sudo apt-get install -y python-dev

  - name: Instalar requirements
	command: sudo pip install -r proyectoIV/requirements.txt

 - name: Creamos y damos permisos al directorio log
    file: path=/home/dabrase/proyectoIV/log state=directory mode="0777"

  - name: Creamos y damos permisos a archivo logs.txt
    file: path=/home/dabrase/IV/log/logs.txt state=touch mode="u+rwx,g+rwx,o+rwx"

  - name: Ejecutar supervisor
	service: name=supervisor state=started
```
Este archivo lo que hace es instalar paquetes necesarios para ejecutar nuestra aplicación.


### Fabric

Fabric es una biblioteca en linea de comandos para realizar despliegues por SSH ([sitio oficial](http://www.fabfile.org/))

Para instalar fabric:

``
sudo apt-get install fabric

``
Necesitamos un archivo llamado [fabfile.py ](https://github.com/dabrase/proyectoIV/blob/master/fabfile.py) para las tareas de Fabric.

Estas tareas son instrucciones que daremos para desplegar.
