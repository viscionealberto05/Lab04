class Cabina:

    def __init__(self, codice_cab, letti, ponte, prezzo):
        self.codice_cab = codice_cab
        self.letti = letti
        self.ponte = ponte
        self.prezzo = prezzo

    def __str__(self):
        return (f"Cabina: {self.codice_cab}, {self.letti} Letti, Ponte {self.ponte}, Prezzo: {self.prezzo} $")

