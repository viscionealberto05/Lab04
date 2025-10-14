from passeggero import Passeggero
from cabina import Cabina
from cabina_deluxe import CabinaSpeciale
#from csv import reader

class Crociera:



    def __init__(self, nome):

        """Inizializza gli attributi e le strutture dati"""

        self._nome = nome
        self.cabine = []
        self.passeggeri = []


    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome


    """Aggiungere setter e getter se necessari"""
    # Aggiunti

    def carica_file_dati(self, file_path):
        """Carica i dati (cabine e passeggeri) dal file"""

        try:    #USARE DUCKTYPING --> magarin fare una funzione (metodo) che prende per argomernto la lista di parametri e dpopo li assegna in auotmatico come attributi
            fileIn = open(file_path,"r",encoding="utf-8")
            for line in fileIn:
                valori = line.strip().split(",")
                if "CAB" in valori[0]:
                    codice_cab = valori[0]
                    letti = valori[1]
                    ponte = valori[2]
                    prezzo = valori[3]
                    if len(valori) == 5:
                        tipologia = valori[4]    #METODO SPECIFICO VALIDO SOLO PER CABINA SPECIALE --> dovrebbe funzionare solo se trova un metodo apposta e capire in uatomatico che c'è una sottoclasse
                        cab = CabinaSpeciale(codice_cab, letti, ponte, prezzo, tipologia)
                    else:
                        cab = Cabina(codice_cab, letti, ponte, prezzo)

                    self.cabine.append(cab)

                else:
                    codice = valori[0]
                    nome = valori[1]
                    cognome = valori[2]
                    passenger = Passeggero(codice, nome, cognome)
                    self.passeggeri.append(passenger)



            fileIn.close()

            liste = [self.passeggeri,self.cabine]

            return liste

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""
        # TODO

    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""
        # TODO


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """
        # TODO

