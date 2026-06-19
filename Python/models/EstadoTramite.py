from datetime import datetime
from typing import Optional
from TipoEstado import TipoEstado

class EstadoTramite:
    cantEstadoTramite=0
    def __init__(self, nombreEstadoTramite, tipoEstado:TipoEstado):
        cantEstadoTramite+=1
        self.__codEstadoTramite=cantEstadoTramite
        self.__nombreEstadoTramite=nombreEstadoTramite
        self.__fechaHoraBajaEstadoTramite:Optional[datetime]=None
        sefl.__tipoEstado=tipoEstado
    
    @property
    def codEstadoTramite(self):
        return self.__fechaHoraBajaEstadoTramite
    
    @property
    def nombreEstadoTramite(self):
        return self.__nombreEstadoTramite
    
    def setNombreEstadoTramite(self, nombreEstadoTramite):
        self.__nombreEstadoTramite= nombreEstadoTramite
    
    @property
    def fechaHoraBajaEstadoTramite(self):
        return self.__fechaHoraBajaEstadoTramite
    
    def setFechaHoraBajaEstadoTramite(self):
        self.__fechaHoraBajaEstadoTramite=datetime.now()
    
    @property
    def tipoEstado(self):
        return self.__tipoEstado