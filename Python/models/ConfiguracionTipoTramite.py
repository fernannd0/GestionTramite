from datetime import datetime
from typing import Optional
from ConfiguracionTipoTramiteEstadoTramite import ConfiguracionTipoTramiteEstadoTramite
from TipoTramite import TipoTramite

class ConfiguracionTipoTramite:
    cantConfiguracionTipoTramite=0
    def __init__(self,tipoTramite:TipoTramite subConfiguraciones[]:ConfiguracionTipoTramiteEstadoTramite):
        cantConfiguracionTipoTramite+=1
        self.__nroConfiguracionTT=cantConfiguracionTipoTramite
        self.__fechaHoraInicioVigenciaTT=datetime.now
        self.__fechaHoraFinVigenciaTT:Optional[datetime]=None
        self.__tipoTramite=tipoTramite
        self.__configuracionesTTET[]=subConfiguraciones

    @property
    def nroConfiguracionTT(self):
        return self.__nroConfiguracionTT
    
    @property
    def fechaHoraInicioVigenciaTT(self):
        return self.__fechaHoraInicioVigenciaTT
    
    @property
    def fechaHoraFinVigenciaTT(self):
        return self.__fechaHoraFinVigenciaTT
    
    def setFechaHoraFinVigenciaTT(self):
        self.__fechaHoraFinVigenciaTT=datetime.now()
    
    @property
    def tipoTramite(self):
        return self.__tipoTramite
    
    @property
    def configuracionesTTET(self):
        return self.__configuracionesTTET
    
    def añadirConfiguracionesTTET(self, configuracionTTET):
        self.__configuracionesTTET.append(configuracionTTTET)
    
    def sacarConfiguracionesTTET(self, configuracionTTET):
        self.__configuracionesTTET.remove(configuracionTTTET)