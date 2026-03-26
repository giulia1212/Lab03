class Dictionary:
    def __init__(self):
        self._dizionario = []        # lista

    def loadDictionary(self,path):
        try:
            with open(path, "r", encoding="utf-8") as file:
                for riga in file:
                    parola = riga.strip()
                    if parola:   # evita le righe vuote
                        self._dizionario.append(parola.lower())
        except FileNotFoundError:
            print("File non trovato!")


    def printAll(self):
        for e in self._dizionario:
            print(e)


    @property
    def dict(self):
        return self._dizionario