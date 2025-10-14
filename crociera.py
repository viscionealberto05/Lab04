from passeggero import Passeggero
from cabina import Cabina
from cabina_deluxe import CabinaDeluxe
from cabina_animali import CabinaAnimali
from assegnazione import Assegnazione
from operator import attrgetter

class Crociera:



    def __init__(self, nome):

        """Inizializza gli attributi e le strutture dati"""

        self._nome = nome
        self.cabine = []
        self.passeggeri = []
        self.assegnazioni = []
        #self.cabine_libere = list(self.cabine)
        #self.passeggeri_liberi = list(self.passeggeri)


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
                    if len(valori) == 5:
                        # Decido “a mano” quale sottoclasse usare a seconda della riga
                        #Chiamo il metodo della classe su una cambina iniziale vuota da riempire
                        if valori[4].isalpha():
                            cab = CabinaDeluxe(None, None, None, None, None).assegnaParametri(valori)
                        else:
                            cab = CabinaAnimali(None, None, None, None, None).assegnaParametri(valori)
                    else:
                        cab = Cabina(None, None, None, None).assegnaParametri(valori)
                    self.cabine.append(cab)

                else:
                    codice = valori[0]
                    nome = valori[1]
                    cognome = valori[2]
                    passenger = Passeggero(codice, nome, cognome)
                    self.passeggeri.append(passenger)

            fileIn.close()

            liste = [self.passeggeri,self.cabine]

            self.cabine_libere = list(self.cabine)
            self.passeggeri_liberi = list(self.passeggeri)

            return liste

        except FileNotFoundError:
            raise FileNotFoundError(f"File {file_path} non trovato")


    def assegna_passeggero_a_cabina(self, codice_cabina, codice_passeggero):
        """Associa una cabina a un passeggero"""

        ExistingPassenger = False
        ExistingCabin = False
        FreePassenger = False
        FreeCabin = False
        Ass_avvenuta = False


        for p in self.passeggeri:
                if p.codice == codice_passeggero:
                    ExistingPassenger = True
                    break

        for c in self.cabine:
                if c.codice_cab == codice_cabina:
                    ExistingCabin = True
                    break

        for p in self.passeggeri_liberi:
                if p.codice == codice_passeggero:
                    FreePassenger = True
                    break

        for c in self.cabine_libere:
                if c.codice_cab == codice_cabina:
                    FreeCabin = True
                    break



        if ExistingPassenger and ExistingCabin and FreeCabin and FreePassenger:
                ass = Assegnazione(codice_cabina,codice_passeggero)
                self.assegnazioni.append(ass)

                for p in enumerate(self.passeggeri_liberi):
                    if p[1].codice == codice_passeggero:
                        self.passeggeri_liberi.pop(p[0])
                    break

                for c in enumerate(self.cabine_libere):
                    if c[1].codice_cab == codice_cabina:
                        self.cabine_libere.pop(c[0])
                    break


                return self.assegnazioni
        else:
            print("Valori inseriti non validi")
            return None


    def cabine_ordinate_per_prezzo(self):
        """Restituisce la lista ordinata delle cabine in base al prezzo"""

        cabine_ordinate = sorted(self.cabine, key=attrgetter("prezzo"))
        return cabine_ordinate


    def elenca_passeggeri(self):
        """Stampa l'elenco dei passeggeri mostrando, per ognuno, la cabina a cui è associato, quando applicabile """

        for p in self.passeggeri:
            for a in self.assegnazioni:
                if a.passeggero == p.codice:
                    print(f"{p}, Cabina Assegnata: {a.cabina}")
                    break
            print(f"{p}")

