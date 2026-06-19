from TipoTramite import TipoTramite
class ConfigCostoTipoTramite:
    def __init__(self, montoBase, tipoTramite:TipoTramite):
        self.__montoCostoBase=montoBase
        self.__tipoTramite=tipoTramite
    
    @property
    def montoCostoBase(self):
        return self.__montoCostoBase
    
    @property
    def tipoTramite(self):
        return self.__tipoTramite