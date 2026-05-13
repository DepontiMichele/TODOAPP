def aggiungi_promemoria(lista_promemoria, testo, importante=False):
    """
    Crea un nuovo promemoria e lo aggiunge alla lista.
    Genera un ID incrementale basato sull'ultimo elemento presente.
    """
    nuovo_id = 1
    if lista_promemoria:
        # Prende l'ID dell'ultimo elemento e aggiunge 1
        nuovo_id = lista_promemoria[-1].get("id", 0) + 1
    
    nuovo_item = {
        "id": nuovo_id,
        "testo": testo,
        "importante": importante,
        "completato": False
    }
    
    lista_promemoria.append(nuovo_item)
    return lista_promemoria

def segna_completato(lista_promemoria, id_promemoria):
    """
    Cerca un promemoria per ID e inverte il suo stato di completamento.
    """
    for item in lista_promemoria:
        if item["id"] == id_promemoria:
            # Inverte lo stato: se era False diventa True, e viceversa
            item["completato"] = not item["completato"]
            return True, lista_promemoria
    
    return False, lista_promemoria

# Test rapido del modulo
if __name__ == "__main__":
    db = []
    db = aggiungi_promemoria(db, "Comprare il latte", importante=True)
    db = aggiungi_promemoria(db, "Fare esercizio", importante=False)
    print("Dopo aggiunta:", db)
    
    successo, db = segna_completato(db, 1)
    print("Dopo aver completato il primo:", db)