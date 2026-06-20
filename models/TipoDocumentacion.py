from datetime import datetime
from typing import Optional
class TipoDocumentacion:
    def __init__(self, nombreTipoDocumentacion, requiereEntregaWeb:bool, codTipoDocumentacion:int=0, fechaHoraBajaTipoDocumentacion:Optional[datetime]=None):
        self.__codTipoDocumentacion=codTipoDocumentacion
        self.__fechaHoraBajaTipoDocumentacion=fechaHoraBajaTipoDocumentacion
        self.__nombreTipoDocumentacion=nombreTipoDocumentacion
        self.__requiereEntregaWeb=requiereEntregaWeb

    
    def __str__(self):
        return f"""
                ______TipoDocumentacion__________________
                codigo: {self.__codTipoDocumentacion} 
                nombre: {self.__nombreTipoDocumentacion}
                requiere entrega web: {self.__requiereEntregaWeb}
                fecha de Baja: {self.__fechaHoraBajaTipoDocumentacion}
                ________________________________________
                """
    
    @property
    def codTipoDocumentacion(self):
        return self.__codTipoDocumentacion
    
    @property
    def fechaHoraBajaTipoDocumentacion(self):
        return self.__fechaHoraBajaTipoDocumentacion
    
    def setFechaHoraBajaTipoDocumentacion(self):
        self.__fechaHoraBajaTipoDocumentacion=datetime.now()
    
    @property
    def nombreTipoDocumentacion(self):
        return self.__nombreTipoDocumentacion
    
    def setNombreTipoDocumentacion(self, nombre):
        self.__nombreTipoDocumentacion=nombre
    
    @property
    def requiereEntregaWeb(self):
        return self.__requiereEntregaWeb
    
    def setRequiereEntregaWeb(self, valor:bool):
        self.__requiereEntregaWeb=valor

