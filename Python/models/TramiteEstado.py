from datetime import datetime
from typing import Optional
from EstadoTramite import EstadoTramite

class TramiteEstado:
    def __init__(self, observaciones, contadorTramiteEstado=1, estadoTramite:EstadoTramite):
        self.__fechaHoraInicioTramiteEstado=datetime.now()
        self.__fechaHoraFinTramiteEstado:Optional[datetime]=None
        self.__observaciones=observaciones
        self.__contadorTramiteEstado=contadorTramiteEstado
        self.__estadoTramite=estadoTramite

    @property
    def fechaHoraInicioTramiteEstado(self):
        self.__fechaHoraInicioTramiteEstado
    
    @property
    def fechaHoraFinTramiteEstado(self):
        return self.__fechaHoraFinTramiteEstado
    
    def setFechaHoraFinTramiteEstado(self):
        self.__fechaHoraFinTramiteEstado=datetime.now

    @property
    def observaciones(self):
        return self.__observaciones
    
    def setObservaciones(self, observaciones):
        self.__observaciones=observaciones
    
    @property
    def contadorTramiteEstado(self):
        return self.__contadorTramiteEstado
    
    @property
    def estadoTramite(self):
        return self.__estadoTramite
    