class TipoEstado:
    def __init__(self, nombreTipoEstado, codTipoEstado:int=0):
        self.__nombreTipoEstado=nombreTipoEstado
        self.__codTipoEstado=codTipoEstado

    def __str__(self):
        return f"""{self.__codTipoEstado}: {self.__nombreTipoEstado}"""

    @property
    def nombreTipoEstado(self):
        return self.__nombreTipoEstado

    @property
    def codTipoEstado(self):
        return self.__codTipoEstado
