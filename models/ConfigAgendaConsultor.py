from Consultor import Consultor
class ConfigAgendaConsultor:
    def __init__(self, cantMaximaTramites, consultor:Consultor):
        self.__cantMaximaTramites
        self.__consultor=consultor
    
    @property
    def cantMaximaTramites(self):
        return self.__cantMaximaTramites
    
    @property
    def consultor(self):
        return self.__consultor
