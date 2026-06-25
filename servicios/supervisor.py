import sys
import os
sys.path.insert(0, os.path.dirname(os.path.dirname(os.path.abspath(__file__))))


from models.TipoTramite import TipoTramite
from models.TipoDocumentacion import TipoDocumentacion
from models.EstadoTramite import EstadoTramite
from models.TipoEstado import TipoEstado
from repositorios.TipoTramiteRepositorio import TipoTramiteRepositorio
from repositorios.TipoDocumentacionRepositorio import TipoDocumentacionRepositorio
from repositorios.EstadoTramiteRepositorio import EstadoTramiteRepositorio
from repositorios.TipoEstadoRepositorio  import TipoEstadoRepositorio


class ServiciosSupervisor:

    def ABMTipoTramite(self):
        self.__repo=TipoTramiteRepositorio()
        while True:
            accion = input("Ingrese la accion a realizar:\n 1.Alta \n 2.Modificar \n 3.Baja \n 4.Salir\n" )
            match accion:

                ##Aqui se crea una instancia de TipoTramite
                case "1": 
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
                case "2":
                    resultado=self.__repo.traerTodosTipoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codsel=input("Ingrese el codigo del tipo de tramite a modificar: ")
                        if len(codsel)>0:
                            codseleccion=int(codsel)
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
                case "3":
                    resultado=self.__repo.traerTodosTipoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codsel=input("Ingrese el codigo del tipo de tramite a dar de baja: ")
                        if len(codsel)>0:
                            codseleccion=int(codsel)
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
                case "4":
                    break
    
    
    def ABMTipoDocumentacion(self):
        self.__repo=TipoDocumentacionRepositorio()
        while True:
            accion = input("Ingrese la accion a realizar:\n 1.Alta \n 2.Modificar \n 3.Baja \n 4.Salir\n" )
            match accion:

                ##Aqui se crea una instancia de TipoDocumentacion
                case "1": 
                    while True:
                        nombre = input("Ingrese el nombre del Tipo de Documentacion: ")
                        if len(nombre)>0:
                            break
                    while True:
                        web=input("Esta documentacion se ingresa via web? Y/N: ")
                        if web != None:
                            if web.lower()=="y":
                                requiereWeb=True
                                break
                            elif web.lower()=="n":
                                requiereWeb=False
                                break
                        
                    r=self.__repo.buscarTipoDocumentacion(nombre)
                    flag=False ##Me va a indicar si debo crear el Tipo de Documentacion
                    if len(r)==0:
                        flag = True    
                    else: 
                        
                        print("""
                        ---------------------------------------------
                              Tipo de Documentaciones existentes
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
                        t1=TipoDocumentacion(nombre, requiereWeb)
                        self.__repo.darAltaTipoDocumentacion(t1)
                        print("""
                        ------------------------------------------------
                        Tipo de Documentacion dado de alta exitosamente
                        ------------------------------------------------""")
                    continue
                    



                ##Aqui modifico una instancia existente
                case "2":
                    resultado=self.__repo.traerTodosTipoDocumentacion()

                    for x in resultado:
                        print(x)

                    while True:
                        codsel=input("Ingrese el codigo del tipo de Documentacion a modificar: ")
                        if len(codsel)>0:
                            codseleccion=int(codsel)
                            break
                    seleccionTD=self.__repo.buscarTipoDocumentacion(codseleccion)

                    nombre = input("Ingrese el nombre del Tipo de Documentacion o si esta bien deje vacio: ")
                    if len(nombre)>0:
                        seleccionTD.setNombreTipoDocumentacion(nombre)

                    while True:
                        web=input("Esta documentacion se ingresa via web? Y/N: ")
                        if web != None:
                            if web.lower()=="y":
                                requiereWeb=True
                                break
                            elif web.lower()=="n":
                                requiereWeb=False
                                break
                    
                    seleccionTD.setRequiereEntregaWeb(requiereWeb)

                    self.__repo.actualizarTipoDocumentacion(seleccionTD)
                    print("""
                        -----------------------------------------------
                        Tipo de Documentacion modificado exitosamente
                        -----------------------------------------------""")
                    continue


                ##Aqui voy a dar de baja
                case "3":
                    resultado=self.__repo.traerTodosTipoDocumentacion()

                    for x in resultado:
                        print(x)

                    while True:
                        codseleccion=int(input("Ingrese el codigo del tipo de Documentacion a dar de baja: "))
                        if codseleccion !=  None:
                            break
                    seleccionTD=self.__repo.buscarTipoDocumentacion(codseleccion)

                    if seleccionTD.fechaHoraBajaTipoDocumentacion is not None:
                        print("""
                        ---------------------------------------------------
                        Tipo de Documentacion ya se encuentra dado de baja
                        ---------------------------------------------------""")
                        
                        continue

                    seleccionTD.setFechaHoraBajaTipoDocumentacion()
                    self.__repo.darBajaTipoDocumentacion(seleccionTD)
                    print("""
                        -------------------------------------------------
                        Tipo de Documentacion dado de baja exitosamente
                        -------------------------------------------------""")
                    continue


                ##Aqui para cuando quiere salir del CU
                case "4":
                    break


    def ABMEstadoTramite(self):
        self.__repoET=EstadoTramiteRepositorio()
        self.__repoTE=TipoEstadoRepositorio()
        while True:
            accion = input("Ingrese la accion a realizar:\n 1.Alta \n 2.Modificar \n 3.Baja \n 4.Salir\n" )
            match accion:

                ##Aqui se crea una instancia de EstadoTramite
                case "1": 
                    while True:
                        nombre = input("Ingrese el nombre del Estado de Tramite: ")
                        if len(nombre)>0:
                            break
                    while True:
                        listate=self.__repoTE.traerTodosTipoEstado()
                        for a in listate:
                            print(a)
                        te=input("Ingrese el numero del tipo de estado: ")
                        if len(te)>0:
                            selte=int(te)
                            break
                        
                    r=self.__repoET.buscarEstadoTramite(nombre)
                    flag=False ##Me va a indicar si debo crear el Estado Tramite
                    if len(r)==0:
                        flag = True    
                    else: 
                        
                        print("""
                        ---------------------------------------------
                                  Estados Tramites existentes
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
                        te=self.__repoTE.buscarTipoEstado(selte)
                        et1=EstadoTramite(nombre,te )
                        self.__repoET.darAltaEstadoTramite(et1)
                        print("""
                        ------------------------------------------------
                          Estado de Tramite dado de alta exitosamente
                        ------------------------------------------------""")
                    continue
                    



                ##Aqui modifico una instancia existente
                case "2":
                    resultado=self.__repoET.traerTodosEstadoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codsel=input("Ingrese el codigo del estado tramite a modificar: ")
                        if len(codsel)>0:
                            codseleccion=int(codsel)
                            break
                    seleccionET=self.__repoET.buscarEstadoTramite(codseleccion)

                    nombre = input("Ingrese el nombre del Estado de Tramite o si esta bien deje vacio: ")
                    if len(nombre)>0:
                        seleccionET.setNombreEstadoTramite(nombre)
                        

                    listate=self.__repoTE.traerTodosTipoEstado()
                    for x in listate:
                        print(x)

                    codte=input("Ingrese el numero del tipo de estado o si ya esta bien deje vacio: ")
                    if len(codte)>0:
                        codtesel=int(codte)
                        te=self.__repoTE.buscarTipoEstado(codtesel)
                        seleccionET.setTipoEstado(te)
                    

                    

                    self.__repoET.actualizarEstadoTramite(seleccionET)
                    print("""
                        -----------------------------------------------
                            Estado Tramite modificado exitosamente
                        -----------------------------------------------""")
                    continue


                ##Aqui voy a dar de baja
                case "3":
                    resultado=self.__repoET.traerTodosEstadoTramite()

                    for x in resultado:
                        print(x)

                    while True:
                        codseleccion=input("Ingrese el codigo del Estado Tramite a dar de baja: ")
                        if len(codseleccion)>0:
                            codsel=int(codseleccion)
                            break
                    seleccionET=self.__repoET.buscarEstadoTramite(codsel)

                    if seleccionET.fechaHoraBajaEstadoTramite is not None:
                        print("""
                        ---------------------------------------------------
                            Estado Tramite ya se encuentra dado de baja
                        ---------------------------------------------------""")
                        
                        continue

                    seleccionET.setFechaHoraBajaEstadoTramite()
                    self.__repoET.darBajaEstadoTramite(seleccionET)
                    print("""
                        -------------------------------------------------
                            Estado Tramite dado de baja exitosamente
                        -------------------------------------------------""")
                    continue


                ##Aqui para cuando quiere salir del CU
                case "4":
                    break

 
    def ConfigurarTipoTramite(self):
        while True:
            accion=input("Ingrese la accion a realizar:\n 1.Nueva configuracion\n 2. Modificar configuracion\n")
            match accion:
                case "1":
                    
