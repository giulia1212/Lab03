import dictionary as d
import richWord as rw


class MultiDictionary:

    def __init__(self):
        # creo un dizionario di dizionari
        self.dizionari = {
            "italian": d.Dictionary(),
            "english": d.Dictionary(),
            "spanish": d.Dictionary()
        }
        # ora riempio i dizionari
        self.dizionari["italian"].loadDictionary("resources/Italian.txt")
        self.dizionari["english"].loadDictionary("resources/English.txt")
        self.dizionari["spanish"].loadDictionary("resources/Spanish.txt")

    def printDic(self, language):
        if language.lower() not in self.dizionari:
            print("La lingua da te scelta non è supportata!")
            return
        for word in self.dizionari[language.lower()].dict:
            print(word, end=" ")

    def searchWord(self, words, language):
        risultato = []
        language = language.lower()
        if language not in self.dizionari:
            print("La lingua da te scelta non è supportata!")
            return risultato
        dizionario_lingua = self.dizionari[language].dict
        for word in words:
            richword = rw.RichWord(word)
            richword.corretta = word in dizionario_lingua
            risultato.append(richword)

        return risultato

    def searchWordLinear(self, words, language):
        """Iterare su tutti gli elementi del vocabolario a partire dal primo. La ricerca termina quando viene trovato
        l’elemento cercato o si raggiunge l’ultimo, nel caso in cui l’elemento cercato non sia presente nella lista."""
        risultato = []
        language = language.lower()
        if language not in self.dizionari:
            print("La lingua da te scelta non è supportata!")
            return risultato
        dizionario_lingua = self.dizionari[language].dict

        for word in words:
            richword = rw.RichWord(word)
            # Ricerca lineare esplicita
            richword.corretta = False
            for w in dizionario_lingua:
                if w == word:
                    richword.corretta = True
                    break
            risultato.append(richword)

        return risultato

    def searchWordDichotomic(self, words, language):
        """Sapendo che il vocabolario è ordinato alfabeticamente, l'idea è quella di non iniziare la ricerca dal primo
            elemento, ma da quello centrale, cioè a metà del dizionario. Si confronta questo elemento con quello cercato:
                - Se corrisponde, la ricerca termina indicando che l'elemento è stato trovato
                - se è superiore, la ricerca viene ripetuta sugli elementi precedenti (ovvero sulla prima metà del
                    dizionario), scartando quelli successivi
                - se è inferiore, la ricerca viene ripetuta sugli elementi successivi (ovvero sulla seconda metà del
                    dizionario), scartando quelli precedenti.
            Il procedimento viene ripetuto iterativamente fino a quando o si trova l’elemento cercato, o tutti gli elementi
            vengono scartati.
            In quest’ultimo caso la ricerca termina indicando che il valore non è stato trovato."""
        risultato = []
        language = language.lower()
        if language not in self.dizionari:
            print("La lingua da te scelta non è supportata!")
            return risultato

        dizionario_lingua = sorted(self.dizionari[language].dict)  # ordiniamo il dizionario

        for word in words:
            richword = rw.RichWord(word)
            low = 0
            high = len(dizionario_lingua) - 1
            richword.corretta = False
            while low <= high:
                mid = (low + high) // 2
                if dizionario_lingua[mid] == word:
                    richword.corretta = True
                    break
                elif dizionario_lingua[mid] < word:
                    low = mid + 1
                else:
                    high = mid - 1
            risultato.append(richword)

        return risultato


