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

while True:
    seguir = int(input("¿Desea volver a ver las opciones? 1=si 2=no: "))
    if seguir == 1:
        accion.opcion()
    elif seguir==2:
        print("Adios!")
        break
    else:
        print("Opcion erronea")


