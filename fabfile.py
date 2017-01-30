from fabric.api import *
import os

def info_servidor():
    run ('uname -s')

def descargar():
    run ('sudo rm -rf proyectoIV/')
    run ('git clone https://github.com/dabrase/proyectoIV.git')

def actualizar():
    run ('cd proyectoIV/')
    run ('sudo git pull')

def borrar():
    run ('sudo rm -rf proyectoIV/')

def instalar():
    run ('cd proyectoIV/ && pip install -r requirements.txt')

def consultar_contenido():
    run ('cd proyectoIV/ && ls -la')

def iniciar():
        run ('sudo supervisorctl start ElMeteo_bot')

def stop():
    run("sudo supervisorctl stop ElMeteo_bot")

def status():
    run("sudo supervisorctl status ElMeteo_bot")

def recargar():
    run("sudo supervisorctl reload")

def testear():
        run ('cd proyectoIV/ &&  python ElMeteo_bot/test_bd.py')

def iniciar_hup():
	run ('nohup python proyectoIV/ElMeteo_bot/bot.py >& /dev/null &',pty=False)

