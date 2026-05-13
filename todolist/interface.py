def mostra_menu():
    """Stampa le opzioni disponibili nel terminale."""
    print("\n" + "="*30)
    print("     📌 TOOL PROMEMORIA")
    print("="*30)
    print("1. Visualizza promemoria")
    print("2. Aggiungi nuovo")
    print("3. Segna come completato/da fare")
    print("4. Esci")
    print("="*30)

def stampa_lista(lista_promemoria):
    """
    Mostra i promemoria ordinati: 
    Prima quelli importanti, poi gli altri.
    """
    if not lista_promemoria:
        print("\n📭 La lista è vuota. Goditi il tuo tempo libero!")
        return

    # LOGICA DI ORDINAMENTO: 
    # Python ordina i booleani mettendo True dopo False. 
    # Usando reverse=True, i True (importanti) finiscono in cima.
    lista_ordinata = sorted(lista_promemoria, key=lambda x: x['importante'], reverse=True)

    print("\n--- I TUOI PROMEMORIA ---")
    for p in lista_ordinata:
        # Icona per l'importanza
        prefisso = "🔥 [IMPORTANTE]" if p['importante'] else "📝"
        
        # Icona per il completamento
        stato = "[X]" if p['completato'] else "[ ]"
        
        # Formattazione della riga
        print(f"{p['id']}. {stato} {prefisso} {p['testo']}")
    print("------------------------")

def richiedi_input(messaggio):
    """Semplice wrapper per l'input utente."""
    return input(messaggio)