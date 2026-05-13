def ordina_importanti(lista):
    lista_importanti = []
    lista_nonImportanti = []
    for promemoria in lista:
        if(promemoria["isImportant"] == True):
            lista_importanti.append(promemoria)
        else:
            lista_nonImportanti.append(promemoria)
    return lista_importanti + lista_nonImportanti