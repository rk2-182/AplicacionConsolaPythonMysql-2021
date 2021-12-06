import os
import time
from usuario import Usuario 

class Acciones:
    
    def opcion(self):

            print("Acciones Dispobibles: ")
            print("-Registro")
            print("-Login")
            try:
                while True:
                    accion = int(input("Ingrese su opcion: (1 Registro o 2 Login)"))
                    if accion == 1:
                        print("Ingresando al registro...")
                        #Clase acciones llama al metdo registro
                        coleccionDeDatos=Acciones.__registro(self)
                        #print(coleccionDeDatos[0])
                        
                        usuario = Usuario(coleccionDeDatos[0],coleccionDeDatos[1],coleccionDeDatos[2],coleccionDeDatos[3])

                        registro=usuario.registrarUsuario()

                        if len(registro) >=1:
                            print("Regristro exitoso")
                        else:
                            print("Ha ocurrido un error")  

                        break
                    elif accion == 2:
                        print("Ingresando a Login...")
                        Acciones.__login(self)
                        break
                    else:
                        print("La opcion ingresada no existe!, vuelva a intentarlo.")
                
            except ValueError:
                print("El valor ingresado no es correcto, vuelva a ingresarlo")
                time.sleep(3)
                os.system('cls')
                self.opcion()

    #metodo privado
    def __registro(self):
        
        nombre = input("Ingresa tu Nombre: ")
        apellido = input("Ingresa tu apellido: ")
        email = input("Ingresa tu email: ")
        password = input("Introduce tu contraseña: ")

        return [nombre,apellido,email,password] #retornar una lista con los datos ingresados

    def __login(self):
        email = input("Introduce tu email: ")
        password = input("Introduce tu contraseña: ")
