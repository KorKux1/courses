class CasillaVotacion:
    def __init__(self, indentificador,pais):
        self._identificador = indentificador
        self._pais = pais
        self._region = None

    @property
    def region(self):
        return self._region
    
    @region.setter
    def region(self,reg):
        if reg in self._pais:
            self._region = reg
        else:
            raise ValueError(f'La region {reg} no es valida en {self._pais}')

casilla = CasillaVotacion(123,['Bogota','Cali'])
print(casilla.region)
casilla.region = 'Bogota'
print(casilla.region)