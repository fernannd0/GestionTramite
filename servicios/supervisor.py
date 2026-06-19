import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from models.TipoTramite import TipoTramite
from repositorios.TipoTramiteRepositorio import TipoTramiteRespositorio

class ServiciosSupervisor:


    def __init__(self):
        self.__repo=TipoTramiteRespositorio()



    def ABMTipoTramite(self):
        while True:
            accion = int(input("Ingrese la accion a realizar:\n 1.Alta \n 2.Modificar \n 3.Baja \n 4.Salir\n" ))
            match accion:

                ##Aqui se crea una instancia de TipoTramite
                case 1: 
                    while True:
                        nombre = input("Ingrese el nombre del Tipo de Tramite: ")
                        if len(nombre)>0:
                            break
                    while True:
                        cant=input("Ingrese la cantidad de dias que tiene este tipo de tramite para entregar la documentacion: ")
                        if cant != None:
                            cantidadDias=int(cant)
                            break
                    r=self.__repo.buscarTipoTramite(nombre)
                    flag=False ##Me va a indicar si debo crear el Tipo de Tramite
                    if len(r)==0:
                        flag = True    
                    else: 
                        
                        print("""
                        ---------------------------------------------
                                 Tipo de Tramites existentes
                        ---------------------------------------------""")
                        for x in r:
                            print(x)
                        while True:
                            accion=input(f"Desea dar de alta {nombre}? Y/N:  ").lower()
                            if accion=="y":
                                flag=True
                                break
                            elif accion=="n":
                                break
                        
                    if flag:    
                        t1=TipoTramite(nombre, cantidadDias)
                        self.__repo.darAltaTipoTramite(t1)
                        print("""
                        ---------------------------------------------
                          Tipo de Tramite dado de alta exitosamente
                        ---------------------------------------------""")
                    continue
                    



                ##Aqui modifico una instancia existente
                case 2:
                    resultado=self.__repo.traerTodosTipoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codseleccion=int(input("Ingrese el codigo del tipo de tramite a modificar: "))
                        if codseleccion !=  None:
                            break
                    seleccionTT=self.__repo.buscarTipoTramite(codseleccion)

                    nombre = input("Ingrese el nombre del Tipo de Tramite o si esta bien deje vacio: ")
                    if len(nombre)>0:
                        seleccionTT.setNombreTipoTramite(nombre)

                    cantidadDias=input("Ingrese la cantidad de dias que tiene este tipo de tramite para entregar la documentacion o si esta bien deje vacio: ")
                    if cantidadDias != None:
                        cant=int(cantidadDias)
                        seleccionTT.setCantidadDiasMaximoDocumentacion(cant)

                    self.__repo.actualizarTipoTramite(seleccionTT)
                    print("""
                        ---------------------------------------------
                          Tipo de Tramite modificado exitosamente
                        ---------------------------------------------""")
                    continue


                ##Aqui voy a dar de baja
                case 3:
                    resultado=self.__repo.traerTodosTipoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codseleccion=int(input("Ingrese el codigo del tipo de tramite a dar de baja: "))
                        if codseleccion !=  None:
                            break
                    seleccionTT=self.__repo.buscarTipoTramite(codseleccion)

                    if seleccionTT.fechaHoraBajaTT is not None:
                        print("""
                        ---------------------------------------------
                        Tipo de Tramite ya se encuentra dado de baja
                        ---------------------------------------------""")
                        
                        continue

                    seleccionTT.setFechaHoraBajaTT()
                    self.__repo.darBajaTipoTramite(seleccionTT)
                    print("""
                        ---------------------------------------------
                          Tipo de Tramite dado de baja exitosamente
                        ---------------------------------------------""")
                    continue


                ##Aqui para cuando quiere salir del CU
                case 4:
                    break

