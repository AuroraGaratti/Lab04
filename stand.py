class Stand:
    def __init__(self, codice, dimensione, padiglione, prezzo):
        self.codice=codice
        self.dimensione=dimensione
        self.padiglione=padiglione
        self._prezzo=float(prezzo)
        self.disponibile=True
        self.espositore=None

    @property
    def prezzo(self):
        return self._prezzo

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return (f"{self.codice}: Standard | {self.dimensione} mq - Padiglione {self.padiglione} "
                f"- Prezzo {self.prezzo}€ - {stato}")

    def __repr__(self):
        return f"[{self.__str__()}]"

    def __lt__(self,other):
        return self.prezzo < other.prezzo
    #indica criterio paragone non metto isinstance appartengono alla stessa classe

class StandPremium(Stand):
    def __init__(self, codice, dimensione, padiglione, prezzo, posizione):
        super().__init__(codice, dimensione, padiglione, prezzo)
        self.posizione=posizione

    @property
    def prezzo(self):
        return self._prezzo * 1.30

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return (f"{self.codice}: Premium | {self.dimensione} mq - Padiglione {self.padiglione} "
                f"- Prezzo {self.prezzo}€ - Posizione: {self.posizione} - {stato}")

    def __repr__(self):
        return f"[{self.__str__()}]"

class StandPrese(Stand):
    def __init__(self, codice, dimensione, padiglione, prezzo, num_prese):
        super().__init__(codice, dimensione, padiglione, prezzo)
        self.num_prese=int(num_prese)

    @property
    def prezzo(self):
        return self._prezzo * (1 + 0.07 * self.num_prese)

    def __str__(self):
        stato = "Disponibile" if self.disponibile else "Non disponibile"
        return (f"{self.codice}: Prese extra | {self.dimensione} mq - Padiglione {self.padiglione} "
                f"- Prezzo {self.prezzo}€ - Prese aggiuntive: {self.num_prese} - {stato}")

    def __repr__(self):
        return f"[{self.__str__()}]"

