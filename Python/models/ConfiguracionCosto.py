from datetime import datetime
from typing import Optional
from ConfigCostoTipoTramite import ConfigCostoTipoTramite

class ConfiguracionCosto:
    cantConfiguracionCosto=0
    def __init__(self, fechaInicio:datetime, fechaFin:Optional[datetime]=None, subconfiguraciones[]:ConfigCostoTipoTramite):
        cantConfiguracionCosto+=1
        self.__nroConfiguracionCosto=cantConfiguracionCosto
        self.__fechaHoraInicioVigenciaCosto=fechaInicio
        self.__fechaHoraFinVigenciaCosto=fechaFin
        self.__configCostoTipoTramite[]=subconfiguraciones

    @property
    def nroConfiguracionCosto(self):
        return self.__nroConfiguracionCosto
    
    @property
    def fechaHoraInicioVigenciaCosto(self):
        return self.__fechaHoraInicioVigenciaCosto
    
    @property
    def fechaHoraFinVigenciaCosto(self):
        return self.__fechaHoraFinVigenciaCosto
    
    def setFechaHoraFinVigenciaCosto(self):
        self.__fechaHoraFinVigenciaCosto=datetime.now()
    
    @property
    def configCostoTipoTramite(self):
        return self.__configCostoTipoTramite
    
    def añadirCostoTipoTramite(self, costoTipoTramite:ConfigCostoTipoTramite):
        self.__configCostoTipoTramite.append(costoTipoTramite)
    
    def sacarCostoTipoTramite(self, costoTipoTramite:ConfigCostoTipoTramite):
        self.__configCostoTipoTramite.remove(costoTipoTramite)