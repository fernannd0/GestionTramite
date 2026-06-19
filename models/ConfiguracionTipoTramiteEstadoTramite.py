from EstadoTramite import EstadoTramite

class ConfiguracionTipoTramiteEstadoTramite:
    def __init__(self, orden, estadoTramite:EstadoTramite):
        self.__ordenTipoTramiteEstadoTramite=orden
        self.__estadoTramite=estadoTramite

    @property
    def ordenTipoTramiteEstadoTramite(self):
        return self.__ordenTipoTramiteEstadoTramite
    
    @property
    def estadoTramite(self):
        return self.__estadoTramite
    