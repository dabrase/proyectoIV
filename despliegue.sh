#!/bin/bash

#Actualizar apt
sudo apt-get update

#Instalar vagrant
sudo apt-get install -y vagrant

#Instalar el plugin vagrant-azure
sudo vagrant plugin install vagrant-azure

#Instalar pip
curl "https://bootstrap.pypa.io/get-pip.py" -o "get-pip.py"
sudo python get-pip.py

#Instalar ansible
sudo apt-get install -y ansible

#Instalar fabric
sudo apt-get install -y fabric

#Descargar azure box
vagrant box add azure https://github.com/msopentech/vagrant-azure/raw/master/dummy.box

# Creación y provisionamiento de la máquina virtual con vagrant y ansible
vagrant up --provider=azure


#Despliegue y ejecución de la aplicación con fabric
fab -p 0123456Granada -H dabrase@elmeteobot.cloudapp.net iniciar_hup
