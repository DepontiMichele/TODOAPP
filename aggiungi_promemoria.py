import json
import os

def aggiungi_task(nome_file="tasks.json"):
    """
    Funzione interattiva per aggiungere una task.
    Gestisce ID progressivi, scadenze facoltative e importanza.
    """
    # 1. Caricamento dati esistenti
    tasks = []
    if os.path.exists(nome_file):
        with open(nome_file, "r", encoding="utf-8") as f:
            try:
                tasks = json.load(f)
            except json.JSONDecodeError:
                tasks = []

    # 2. Input da tastiera
    print("\n--- NUOVA TASK ---")
    descrizione = input("Cosa devi fare? ")
    
    # Data come scadenza: se preme invio, resta stringa vuota
    scadenza = input("Scadenza (es. 25/12/2026) o premi INVIO per nessuna: ").strip()
    
    # Importanza
    scelta_importante = input("È una task importante? (s/n): ").lower().strip()
    importante = True if scelta_importante == 's' else False

    # 3. Calcolo ID numerico progressivo
    # Troviamo l'ID più alto presente per evitare duplicati
    if not tasks:
        nuovo_id = 1
    else:
        nuovo_id = max(t['id'] for t in tasks) + 1

    # 4. Creazione del dizionario (Record)
    nuova_task = {
        "id": nuovo_id,
        "descrizione": descrizione,
        "scadenza": scadenza,  # Sarà "" se non inserita
        "importante": importante,
        "completata": False
    }

    # 5. Salvataggio su file JSON
    tasks.append(nuova_task)
    
    try:
        with open(nome_file, "w", encoding="utf-8") as f:
            json.dump(tasks, f, indent=4, ensure_ascii=False)
        print(f"\n✅ Task #{nuovo_id} salvata con successo!")
    except Exception as e:
        print(f"❌ Errore durante il salvataggio: {e}")