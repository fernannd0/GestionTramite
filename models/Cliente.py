from datetime import datetime
from typing import Optional

class Cliente:
    cantCliente=0
    def __init__(self, dni:int, nombreApellidoCliente, emailCliente):
        cantCliente+=1
        self.__codUsuario=cantCliente
        self.__dniCliente=dni
        self.__nombreApellidoCliente=nombreApellidoCliente
        self.__emailCliente=emailCliente
        self.__fechaHoraBajaCliente:Optional[datetime]=None

    @property
    def codUsuario(self):
        return self.__codUsuario
    
    @property
    def dniCliente(self):
        return self.__dniCliente
    
    def setDniCliente(self, dni):
        self.__dniCliente=dni

    @property
    def nombreApellidoCliente(self):
        return self.__nombreApellidoCliente
    
    def setNombreApellidoCliente(self, nombreApellidoCliente):
        self.__nombreApellidoCliente=nombreApellidoCliente
    
    @property
    def emailCliente(self):
        return self.__emailCliente

    def setEmailCliente(self, emailCliente):
        self.__emailCliente=emailCliente
    
    @property
    def fechaHoraBajaCliente(self):
        return self.__fechaHoraBajaCliente
    
    def setFechaHoraBajaCliente(self):
        self.__fechaHoraBajaCliente=datetime.now()