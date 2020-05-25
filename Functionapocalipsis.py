armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}

def balas(cargadores, armas):
    listaparacomparar = []
    listacargadores = list(cargadores)
    total = 0
    for i in listacargadores:
        if i in armas:
            listaparacomparar.append(i)
    for i in listaparacomparar:
        if i in cargadores:
            suma = sum(cargadores[i])
            total+=suma
    return total

print(balas(cargadores, armas))