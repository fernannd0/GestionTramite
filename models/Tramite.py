from datetime import datetime, timedelta
from typing import Optional
from Cliente import Cliente
from Consultor import Consultor
from TramiteDocumentacion import TramiteDocumentacion
from TipoTramite import TipoTramite
from EstadoTramite import EstadoTramite
from TramiteEstado import TramiteEstado


class Tramite:
    cantidadTramite=0
    def __init__(cantidadDiasMaximoDocumentacion:int, observaciones='', cliente:Cliente, consultor:Consultor, tipoTramite:TipoTramite, estadoTramite:EstadoTramite, tramiteEstado:TramiteEstado):
        Tramite.cantidadTramite+=1
        self.__numeroTramite= Tramite.cantidadTramite
        self.__fechaHoraIngresoTramite=datetime.now()
        self.__fechaHoraFinReal: Optional[datetime]=None
        self.__fechaHoraInicioReal: Optional[datetime]=None
        self.__observaciones=observaciones
        self.__fechaHoraLimiteDocumentacion=datetime.now()+timedelta(days=cantidadDiasMaximoDocumentacion)
        self.__cliente=cliente
        self.__consultor=Consultor
        self.__tramiteDocumentacion=[]
        self.__tipoTramite=tipoTramite
        self.__estadoTramite=estadoTramite
        self.__tramiteEstado=[tramiteEstado]

    @property
    def numeroTramite(self):
        return self.__numeroTramite

    @property
    def fechaHoraIngresoTramite(self):
        return self.__fechaHoraIngresoTramite

    @property
    def fechaHoraFinReal(self):
        return self.__fechaHoraFinReal
    
    def setFechaHoraFinReal(self):
        self.__fechaHoraFinReal=datetime.now()
    
    @property
    def fechaHoraInicioReal(self):
        return self.__fechaHoraInicioReal
    
    def setFechaInicioReal(self):
        self.__fechaHoraInicioReal=datetime.now()
    
    def setObservaciones(self, observaciones):
        self.__observaciones=observaciones

    @property
    def fechaHoraLimiteDocumentacion(self):
        return self.__fechaHoraLimiteDocumentacion
    
    @property
    def cliente(self):
        return self.__cliente

    @property
    def consultor(self):
        return self.__consultor
    
    @property
    def tramiteDocumentacion(self):
        return self.__tramiteDocumentacion
    
    def añadirTramiteDocumentacion(self, documentacion:TramiteDocumentacion):
        self.__tramiteDocumentacion.append(documentacion)
    
    def sacarTramiteDocumentacion(self, documentacion:TramiteDocumentacion):
        self.__tramiteDocumentacion.remove(documentacion)
    
    @property
    def tipoTramite(self):
        return self.__tipoTramite
    
    def setTipoTramite(self, tipoTramite):
        self.__tipoTramite=tipoTramite
    
    @property
    def estadoTramite(self):
        return self.__estadoTramite
    
    def setEstadoTramite(self, estadoTramite):
        self.__estadoTramite=estadoTramite

    @property
    def tramiteEstado(self):
        return self.__tramiteEstado
    
    def añadirTramiteEstado(self, tramiteEstado:TramiteEstado):
        self.__tramiteEstado.append(tramiteEstado)