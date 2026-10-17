import csv
from espositori import Espositori
from stand import Stand,StandPremium,StandPrese

class LingottoFiere:
    def __init__(self, nome):
        """Inizializza gli attributi e le strutture dati"""
        self._nome = nome
        self.stand = []
        self.espositori = []

    """Aggiungere setter e getter se necessari"""

    @property
    def nome(self):
        return self._nome

    @nome.setter
    def nome(self, nome):
        self._nome = nome

    def carica_file_dati(self, file_path):
        """Carica i dati (stand ed espositori) dal file"""
        self.espositori.clear()
        self.stand.clear()
        try:
            with open(file_path, "r", encoding = "utf-8") as file:
                elenco=csv.reader(file)
                for riga in elenco:
                    if not riga:
                        continue
                    if riga[0].startswith("ST"):
                        if len(riga) == 4:
                            stand = Stand(riga[0], riga[1], riga[2], riga[3])
                        elif len(riga) == 5 and riga[4].isalpha():
                            stand = StandPremium(riga[0], riga[1], riga[2], riga[3], riga[4])
                        elif len(riga) == 5 and riga[4].isdigit():
                            stand = StandPrese(riga[0], riga[1], riga[2], riga[3], riga[4])
                        self.stand.append(stand)

                    elif riga[0].startswith("ES"):
                        espositore = Espositori(riga[0], riga[1], riga[2])
                        self.espositori.append(espositore)
        
        except FileNotFoundError:
            raise FileNotFoundError("Il file CSV non è stato trovato.")
        #assegnazione oggetti alla lista della classe corrispondete

    def assegna_stand_a_espositore(self, codice_stand, codice_espositore):
        """Associa uno stand a un espositore"""
        stand_selezionato = None
        for stand in self.stand:
            if codice_stand == stand.codice:
                stand_selezionato=stand
                break
        if not stand_selezionato:
            raise Exception ("Stand non trovato")
        if not stand_selezionato.disponibile:
            raise Exception ("Stand non disponibile")
        # esistenza stand e disponibilità

        espositore_selezionato = None
        for espositore in self.espositori:
            if codice_espositore == espositore.codice:
                espositore_selezionato=espositore
                break
        if not espositore_selezionato:
            raise Exception("Espositore non trovato")

        for stand in self.stand:
           if espositore_selezionato == stand.espositore:
                raise Exception("Espositore già associato")
        # esistenza espositore e disponibilità

        stand_selezionato.espositore = espositore_selezionato
        stand_selezionato.disponibile = False
        #associazione stand espositore e aggiornamento stato stand

    def elenca_espositori(self):
        """Stampa l'elenco degli espositori mostrando, per ognuno, lo stand a cui è associato, quando applicabile """
        for espositore in self.espositori:
            for stand in self.stand:
                if espositore == stand.espositore:
                    print(f"{espositore} associato a {stand.codice}")
                    break
            else:
                print(f"{espositore}")

    def stand_ordinati_per_prezzo(self):
        """Restituisce la lista ordinata degli stand in base al prezzo"""
        self.stand.sort()
        return self.stand
        #ordino con __lt__