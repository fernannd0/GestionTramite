from datetime import datetime
from typing import Optional
from models.TipoEstado import TipoEstado

class EstadoTramite:
    def __init__(self, nombreEstadoTramite, tipoEstado:TipoEstado, codEstadoTramite:int=0, fechaHoraBajaEstadoTramite:Optional[datetime]=None):
        self.__codEstadoTramite=codEstadoTramite
        self.__nombreEstadoTramite=nombreEstadoTramite
        self.__fechaHoraBajaEstadoTramite=fechaHoraBajaEstadoTramite
        self.__tipoEstado=tipoEstado

    def __str__(self):
        return f"""
                ______EstadoTramite_____________________
                codigo: {self.__codEstadoTramite}
                nombre: {self.__nombreEstadoTramite}
                tipo de Estado: {self.__tipoEstado.nombreTipoEstado}
                fecha de baja: {self.__fechaHoraBajaEstadoTramite}
                ________________________________________
                """   


    @property
    def codEstadoTramite(self):
        return self.__codEstadoTramite
    
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
    
    def setTipoEstado(self, tipoEstado:TipoEstado):
        self.__tipoEstado=tipoEstado