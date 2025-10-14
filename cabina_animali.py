from cabina import Cabina

class CabinaAnimali(Cabina):

    def __init__(self, codice_cab, letti, ponte, prezzo, animali):
        super().__init__(codice_cab, letti, ponte, prezzo)

        self._animali = animali

    @property
    def animali(self):
        return self._animali

    @animali.setter
    def animali(self, animali):
        self._animali = animali

    def __str__(self):
        return f"{super().__str__()}, Numero animali ammessi: {self._animali}"

    def assegnaParametri(self, valori):
        codice_cab = valori[0]
        letti = valori[1]
        ponte = valori[2]
        prezzo = int(valori[3])*(1+0.1*int(valori[4]))
        animali = valori[4]
        return CabinaAnimali(codice_cab,letti,ponte,prezzo,animali)