class Espositori:
    def __init__(self,codice, nome, cognome):
        self.codice=codice
        self.nome=nome
        self.cognome=cognome

    def __str__(self):
        return f"{self.codice}| Nome: {self.nome} - Cognome: {self.cognome}"

    def __repr__(self):
        return f"[{self.__str__()}]"

    def __eq__(self, other):
        return isinstance(other, Espositori) and self.codice == other.codice
    # chiede se other e espositori appartengono alla stessa classe e indica criterio uguaglianza
