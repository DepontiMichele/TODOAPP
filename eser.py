import os


def mostra_menu():
    print("1. visualizza promemoria")
    print("2. aggiungi promemoria")
    print("3. segna come completato")
    print("4. esci")

def visualizza_lista(lista):
    if not lista:
        print("")
    else:
        print("")
        for i, p in enumerate(lista, 1):
            stato = "fatto" if p["completato"] else "x"
            print(f"{i}. {p['task']} [{stato}]")

def main():
    promemoria = []

    while True:
        mostra_menu()
        scelta = input("\nScegli un'opzione (1-4): ")

        if scelta == "1":
            visualizza_lista(promemoria)
        
        elif scelta == "2":
            testo = input("Cosa devi ricordarti di fare? ")
            promemoria.append({"task": testo, "completato": False})
            print("Aggiunto con successo!")

        elif scelta == "3":
            visualizza_lista(promemoria)
            if promemoria:
                try:
                    indice = int(input("Inserisci il numero del promemoria completato: ")) - 1
                    if 0 <= indice < len(promemoria):
                        promemoria[indice]["completato"] = True
                        print("Ottimo lavoro! Segnato come completato.")
                    else:
                        print("Numero non valido.")
                except ValueError:
                    print("Per favore, inserisci un numero valido.")

        elif scelta == "4":
            print("Arrivederci!")
            break
        
        else:
            print("Opzione non valida, riprova.")

if __name__ == "__main__":
    main()