import json
import os

FILE_PATH = "promemoria.json"

def carica_dati():
    """Carica i promemoria dal file JSON. Se il file non esiste, restituisce una lista vuota."""
    if not os.path.exists(FILE_PATH):
        return []
    
    try:
        with open(FILE_PATH, "r", encoding="utf-8") as file:
            return json.load(file)
    except (json.JSONDecodeError, IOError):
        # In caso di file corrotto o errori di lettura, partiamo da una lista vuota
        return []

def salva_dati(promemoria_list):
    """Salva la lista dei promemoria nel file JSON."""
    try:
        with open(FILE_PATH, "w", encoding="utf-8") as file:
            json.dump(promemoria_list, file, indent=4, ensure_ascii=False)
    except IOError as e:
        print(f"Errore durante il salvataggio dei dati: {e}")

# Esempio di utilizzo rapido per testare il modulo:
if __name__ == "__main__":
    test_data = [{"id": 1, "testo": "Test", "importante": True, "completato": False}]
    salva_dati(test_data)
    print("Dati salvati con successo!")
    print("Dati caricati:", carica_dati())