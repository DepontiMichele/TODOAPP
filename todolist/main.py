import database_manager as db
import logic
import interface

def start_tool():
    # Carichiamo i dati all'inizio (Member 1)
    promemoria_list = db.carica_dati()
    
    while True:
        # Come da tua richiesta, stampiamo sempre la lista all'inizio del ciclo
        interface.stampa_lista(promemoria_list)
        
        interface.mostra_menu()
        scelta = interface.richiedi_input("Scegli un'opzione (1-4): ")

        if scelta == "1":
            # La lista viene già mostrata all'inizio del loop, 
            # ma possiamo aggiungere un messaggio di refresh.
            print("\n Lista aggiornata.")
            
        elif scelta == "2":
            # Aggiunta (Member 2 e 3)
            testo = interface.richiedi_input("Cosa devi ricordare? ")
            imp_input = interface.richiedi_input("È importante? (s/n): ").lower()
            importante = True if imp_input == 's' else False
            
            promemoria_list = logic.aggiungi_promemoria(promemoria_list, testo, importante)
            db.salva_dati(promemoria_list)
            print(" Promemoria aggiunto correttamente!")

        elif scelta == "3":
            # Modifica stato (Member 2 e 3)
            id_input = interface.richiedi_input("Inserisci l'ID del promemoria da segnare: ")
            try:
                id_prom = int(id_input)
                successo, promemoria_list = logic.segna_completato(promemoria_list, id_prom)
                if successo:
                    db.salva_dati(promemoria_list)
                    print(" Stato aggiornato con successo!")
                else:
                    print(" ID non trovato nella lista.")
            except ValueError:
                print(" Errore: Inserisci un numero per l'ID.")

        elif scelta == "4":
            print(" Chiusura del tool. Buon lavoro!")
            break
        
        else:
            print(" Opzione non valida, riprova.")

if __name__ == "__main__":
    start_tool()
