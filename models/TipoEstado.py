class TipoEstado:
    def __init__(self, nombreTipoEstado):
        self.__nombreTipoEstado=nombreTipoEstado

    @property
    def nombreTipoEstado(self):
        return self.__nombreTipoEstado


