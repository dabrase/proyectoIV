### Práctica 0
## 1-Generando tu clave pública SSH:
```
ssh-keygen -t rsa -C "Tu correo electronico"
```
Nos vamos a nuestro perfil de github en el apartado de Setting y en la pestaña "SSH y GPG keys" le damos a añadir clave y en el apartado key copiamos el contenido
de ~/.ssh/id_rsa.pub y le damos a añadir.

##  2- Creación de un repositorio personal para la asignatura y fork del repositorio de la asignatura.
Una vez creada la cuenta en github.com para hospedar nuestro repositorio, vamos a la
pestaña Repositories y creamos un nuevo repositorio. Este será el repositorio remoto.
Una vez creado el repositorio ya podremos trabajar en nuestra maquina local.

##  3- Configurar el nombre y correo electrónico
```
git  config --global user.name "Tu nombre de usuario"
git  config --global user.email "Tu email"

```
##  4- Clonar carpeta de github a nuestro ordenador
Para ello copiamos la direccion de nuestro repositorio. Y en el terminal de nuestro ordenador ejecutamos:
```
git clone https://github.com/dabrase/IV16-17.git

```

## 5- Creación del hito0 en nuestro repositorio personal
Creamos como hito practica0 y creamos la rama para entregar practica0:
```
git remote add upstream https://github.com/dabrase/IV16-17.git
git fetch upstream 
git checkout master 
git checkout -b hito0
git push origin hito0

```
## 6- Añadir archivos
Usamos el comando "add" y para confirmarlo el comando "commit"

```
git add practica0.md
git commit -a -m "Añadido practica0.md"

```
Y para subirlo al remoto usaremos el comando "push"

```
git push

```
