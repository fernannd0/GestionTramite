from datetime import datetime
from typing import Optional

class TipoTramite:
    def __init__(self, nombreTipoTramite:str , cantidadDiasMaximoDocumentacion:int, codTipoTramite:int=0, fechaHoraBajaTT:Optional[datetime]=None):
        self.__codTipoTramite=codTipoTramite
        self.__fechaHoraBajaTT=fechaHoraBajaTT
        self.__nombreTipoTramite=nombreTipoTramite
        self.__cantidadDiasMaximoDocumentacion=cantidadDiasMaximoDocumentacion
    
    def __str__(self):
        return f"""
                ______TipoTramite________________________
                codigo: {self.__codTipoTramite} 
                nombre: {self.__nombreTipoTramite}
                cantidad dias: {self.__cantidadDiasMaximoDocumentacion}
                fecha de Baja: {self.__fechaHoraBajaTT}
                ________________________________________
                """
            
    
    @property
    def codTipoTramite(self):
        return self.__codTipoTramite
    
    @property
    def nombreTipoTramite(self):
        return self.__nombreTipoTramite
    
    def setNombreTipoTramite(self, nombre:str):
        self.__nombreTipoTramite=nombre
        
    @property
    def fechaHoraBajaTT(self):
        return self.__fechaHoraBajaTT
    
    def setFechaHoraBajaTT(self):
        self.__fechaHoraBajaTT=datetime.now()
    
    @property
    def cantidadDiasMaximoDocumentacion(self):
        return self.__cantidadDiasMaximoDocumentacion
    
    def setCantidadDiasMaximoDocumentacion(self, dias:int):
        self.__cantidadDiasMaximoDocumentacion=dias