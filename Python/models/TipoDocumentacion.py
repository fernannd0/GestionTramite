from datetime import datetime
from typing import Optional
class TipoDocumentacion:
    cantTipoDocumentacion=0
    def __init__(self, nombreTipoDocumentacion, requiereEntregaWeb:bool):
        cantTipoDocumentacion+=1
        self.__codTipoDocumentacion=cantTipoDocumentacion
        self.__fechaHoraBajaTipoDocumentacion:Optional[datetime]=None
        self.__nombreTipoDocumentacion=nombreTipoDocumentacion
        self.__requiereEntregaWeb=requiereEntregaWeb
    
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

