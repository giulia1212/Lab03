import spellchecker

sc = spellchecker.SpellChecker()

while True:
    sc.printMenu()
    frase = ""
    lingua = ""
    txtIn = input()
    # Add input control here!
    while not txtIn.isdigit() or int(txtIn) < 1 or int(txtIn) > 4:
        print("Hai inserito un valore non ammesso.")
        print("Inserisci un numero da 1 a 4: ")
        txtIn = input()

    if int(txtIn) == 1:
        print("Inserisci la tua frase in Italiano\n")
        frase = input()
        lingua = "italian"
    elif int(txtIn) == 2:
        print("Inserisci la tua frase in Inglese\n")
        frase = input()
        lingua = "english"
    elif int(txtIn) == 3:
        print("Inserisci la tua frase in Spagnolo\n")
        frase = input()
        lingua = "spanish"

    if int(txtIn) == 4:
        break


    # Esegui il controllo ortografico
    sc.handleSentence(frase, lingua)

    print("\n============================\n")

