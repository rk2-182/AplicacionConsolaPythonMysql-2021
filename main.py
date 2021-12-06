#Proyecto Pythion y MySql
from acciones import Acciones
import os
import time

#Creamos el obejeto para poder usar sus metodos
accion = Acciones()

os.system('cls')
saludo = 'BIENVENIDO'
print(saludo.center(40))
print('------------------------------------------')
accion.opcion()
            


