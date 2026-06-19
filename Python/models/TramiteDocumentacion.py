from datetime import datetime
from TipoDocumentacion import TipoDocumentacion

class TramiteDocumentacion:
    def __init__(self, url, tipoDocumentacion:TipoDocumentacion):
        self.__fechaHoraIngresoDocumentacion=datetime.now()
        self.__urlDocumentacion=url
        self.__tipoDocumentacion=tipoDocumentacion
    
    @property
    def fechaHoraIngresoDocumentacion(self):
        return self.__fechaHoraIngresoDocumentacion
    
    @property
    def urlDocumentacion(self):
        return self.__urlDocumentacion
    
    def setUrlDocumentacion(self, url):
        self.__urlDocumentacion=url
    
    @property
    def tipoDocumentacion(self):
        return self.__tipoDocumentacion
    