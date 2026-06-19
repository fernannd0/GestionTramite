from datetime import datetime
from typing import Optional
from ConfigAgendaConsultor import ConfigAgendaConsultor

class ConfiguracionAgenda:
    cantConfiguracionAgenda=0
    def __init__(self, subconfiguraciones[]:ConfigAgendaConsultor):
        cantConfiguracionAgenda+=1
        self.__nroConfiguracionAgenda= cantConfiguracionAgenda
        self.__fechaHoraInicioVigenciaAgenda=datetime.now()
        self.__fechaHoraFinVigenciaAgenda:Optional[datetime]=None
        self.__configAgendaConsultor[]=subconfiguraciones
    
    @property
    def nroConfiguracionAgenda(self):
        return self.__nroConfiguracionAgenda
    
    @property
    def fechaHoraInicioVigenciaAgenda(self):
        return self.__fechaHoraInicioVigenciaAgenda

    @property
    def fechaHoraFinVigenciaAgenda(self):
        return self.__fechaHoraFinVigenciaAgenda
    
    def setFechaHoraFinVigenciaAgenda(self):
        self.__fechaHoraFinVigenciaAgenda=datetime.now()
    
    @property
    def configAgendaConsultor(self):
        return self.__configAgendaConsultor
    
    def añadirConfigConsultor(self, configConsultor:ConfigAgendaConsultor):
        self.__configAgendaConsultor.append(configConsultor)
    
    def sacarConfigConsultor(self, configConsultor:ConfigAgendaConsultor):
        self.__configAgendaConsultor.remove(configConsultor)