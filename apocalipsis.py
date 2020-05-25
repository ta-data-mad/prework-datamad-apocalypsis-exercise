
#CASO1
armas = ['pistola','escopeta']

cargadores = {
    'pistola': [10, 10], 
    'escopeta': [2, 2, 2, 2, 2]
}
listacargadores = list(cargadores)
listaparacomparar = []
for i in listacargadores:
    total = 0
    if i in armas:
        listaparacomparar.append(i)
for i in listaparacomparar:
    if i in cargadores:
        suma = sum(cargadores[i])
        total+=suma
print(total)    
        
#CASO2
"""armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4]
}
listacargadores = list(cargadores)
listaparacomparar = []
for i in listacargadores:
    total = 0
    if i in armas:
        listaparacomparar.append(i)
for i in listaparacomparar:
    if i in cargadores:
        suma = sum(cargadores[i])
        total+=suma
print(total)
"""
#CASO3:

"""armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1], 
    'fusil de francotirador': [1, 2, 4], 
    'bazoka': [1, 1]
}

listacargadores = list(cargadores)
listaparacomparar = []
for i in listacargadores:
    total = 0
    if i in armas:
        listaparacomparar.append(i)
for i in listaparacomparar:
    if i in cargadores:
        suma = sum(cargadores[i])
        total+=suma
print(total)"""

#CASO4:
"""
armas = ['pistola', 'ametralladora', 'escopeta', 'fusil de francotirador']

cargadores = {
    'pistola': [12, 13, 4, 5, 20, 17], 
    'ametralladora': [33, 40], 
    'escopeta': [2, 2, 2, 1] 
}


listacargadores = list(cargadores)
listaparacomparar = []
for i in listacargadores:
    total = 0
    if i in armas:
        listaparacomparar.append(i)
for i in listaparacomparar:
    if i in cargadores:
        suma = sum(cargadores[i])
        total+=suma
print(total)


for i in armas:
    if i in cargadores:
        print("At least one elemenent was found")
    else:
        print("No element was found")

armas_set = set(armas)
cargadores_set = set(cargadores)

cargadoreslist = []
for i in armas_set.intersection(cargadores_set):
    cargadoreslist.append(i)
print(cargadoreslist)

for i in cargadoreslist:
    for [i] in cargadores:
       """