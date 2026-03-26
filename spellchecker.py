import time

import multiDictionary as md
#import dictionary as d

class SpellChecker:

    def __init__(self):
        self.multiDictionary = md.MultiDictionary()

    def handleSentence(self, txtIn, language):
        fraseFinale = replaceChars(txtIn.lower())
        parole = fraseFinale.strip().split()         # lista con parole della frase inserita in minuscolo

        # -------------- Ricerca con CONTAINS -----------------------
        start_time = time.time()       # inizio tempo
        risultati = self.multiDictionary.searchWord(parole, language)
        print("\nUsing contains")
        numeroErrori = 0
        print("\nParole errate: ")
        for parola in risultati:
            if not parola.corretta:
                print(parola)
                numeroErrori += 1
        end_time = time.time()
        print(f"Il numero di errori di ortografia è {numeroErrori}")
        print(f"Time elapsed {end_time - start_time}")

        # -------------- Ricerca con LINEARE -----------------------
        start_time = time.time()
        risultati = self.multiDictionary.searchWordLinear(parole, language)
        print("\nUsing Linear search")
        numeroErrori = 0
        print("\nParole errate: ")
        for parola in risultati:
            if not parola.corretta:
                print(parola)
                numeroErrori += 1
        end_time = time.time()
        print(f"Il numero di errori di ortografia è {numeroErrori}")
        print(f"Time elapsed {end_time - start_time}")

        # -------------- Ricerca DICOTOMICA -----------------------
        start_time = time.time()
        risultati = self.multiDictionary.searchWordDichotomic(parole, language)
        print("\nUsing Dichotomic search")
        numeroErrori = 0
        print("\nParole errate: ")
        for parola in risultati:
            if not parola.corretta:
                print(parola)
                numeroErrori += 1
        end_time = time.time()
        print(f"Il numero di errori di ortografia è {numeroErrori}")
        print(f"Time elapsed {end_time - start_time}")

    def printMenu(self):
        print("______________________________\n" +
              "      SpellChecker 101\n"+
              "______________________________\n " +
              "Seleziona la lingua desiderata\n"
              "1. Italiano\n" +
              "2. Inglese\n" +
              "3. Spagnolo\n" +
              "4. Exit\n" +
              "______________________________\n")


def replaceChars(text):
    chars = "\\`*_{}[]()>#+-.!$%^;,=_~"
    for c in chars:
        text = text.replace(c, "")
    return text