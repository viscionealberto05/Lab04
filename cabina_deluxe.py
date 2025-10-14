from cabina import Cabina
class CabinaDeluxe(Cabina):
    
    def __init__(self, codice_cab, letti, ponte, prezzo, tipologia):
        
        super().__init__(codice_cab, letti, ponte, prezzo)
        
        self._tipologia = tipologia
    
    @property
    def tipologia(self):
        return self._tipologia
    
    @tipologia.setter
    def tipologia(self, tipologia):
        self._tipologia = tipologia
        
        
    def __str__(self):
        return f"{super().__str__()}, Tipologia Cabina: {self._tipologia}"