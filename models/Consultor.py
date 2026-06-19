from datetime import datetime
from typing import Optional
class Consultor:
    cantConsultor=0
    def __init__(self, nombreApellidoConsultor):
        cantConsultor+=1
        self.__legajoConsultor=cantConsultor
        self.__nombreApellidoConsultor=nombreApellidoConsultor
        self.__fechaHoraBajaConsultor: Optional[datetime]=None
    
    @property
    def legajoConsultor(self):
        return self.__legajoConsultor
    
    @property
    def nombreApellidoConsultor(self):
        return self.__nombreApellidoCliente
    
    def setNombreApellidoConsultor(self, nombreApellidoConsultor)
        self.__nombreApellidoConsultor=nombreApellidoConsultor
    
    @property
    def fechaHoraBajaConsultor(self):
        return self.__fechaHoraBajaConsultor
    
    def setFechaHoraBajaConsultor(self):
        self.__fechaHoraBajaConsultor=datetime.now()