
from TipoDocumentacion import TipoDocumentacion

class TipoTramiteTipoDocumentacion:
    def __init__(self, tipoDocumentacion:TipoDocumentacion):
        self.__tipoDocumentacion=tipoDocumentacion
    
    @property
    def tipoDocumentacion(self):
        self.__tipoDocumentacion
    
    