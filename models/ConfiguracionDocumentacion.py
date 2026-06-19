from datetime import datetime
from typing import Optional
from TipoTramiteTipoDocumentacion import TipoTramiteTipoDocumentacion
from TipoTramite import TipoTramite

class ConfiguracionDocumentacion:
    cantConfiguracionDocumentacion=0
    def __init__(self,tipoTramite:TipoTramite, configuracionesTTTD[]:TipoTramiteTipoDocumentacion):
        cantConfiguracionDocumentacion+=1
        self.__nroConfiguracionDocumentacion=cantConfiguracionDocumentacion
        self.__fechaHoraInicioVigenciaTTTD=datetime.now()
        self.__fechaHoraFinVigenciaTTTD:Optional[datetime]=None
        self.__tipoTramite=tipoTramite
        self.__configuracionesTTTD[]=configuracionesTTTD
    
    @property
    def nroConfiguracionDocumentacion(self):
        return self.__nroConfiguracionDocumentacion
    
    @property
    def fechaHoraInicioVigenciaTTTD(self):
        return self.__fechaHoraInicioVigenciaTTTD
    
    @property
    def fechaHoraFinVigenciaTTTD(self):
        return self.__fechaHoraFinVigenciaTTTD
    
    def setFechaHoraFinVigenciaTTTD(self):
        self.__fechaHoraFinVigenciaTTTD=datetime.now()
    
    @property
    def tipoTramite(self):
        return self.__tipoTramite
    
    @property
    def configuracionesTTTD(self):
        return self.__configuracionesTTTD
    
    def añadirConfiguracionesTTTD(self, configuracionTTTD:TipoTramiteTipoDocumentacion):
        self.__configuracionesTTTD.append(configuracionTTTD)
    
    def     def sacarConfiguracionesTTTD(self, configuracionTTTD:TipoTramiteTipoDocumentacion):
        self.__configuracionesTTTD.remove(configuracionTTTD)
    
