# ejercicio listas

# Metodo propio

lista = [45, 32, 3, 78]
print("lista original:", lista)
#añade un elemento a la lista
lista.append(995)
lista.append(70)
print("lista despues de usar apped: ", lista)
# funcion sort: ordena la lista
lista.sort()
print("lista ordenaada: ", lista)
#funcion reverse: invierte el orden de la lista
lista.reverse()
print("lista al reves", lista)
#funcion exte: añade los elementos de una lista a la lista
lista_extend = [1, 5, 67, 45]
lista.extend(lista_extend)
print("lista despues de estend: ", lista)
# funcion count: cuenta el numero de veces que aparece el elemento indicado como parametrodentro de una lista
print("numero de elmentos 45: ", lista.count(45))
# funcion insert: añade ele elemento pasado como parametro a la lista en la posicion indicada tambien por parametro
lista.insert(4,111)
print("lista despues de insert: ", lista)
#funcion remove: elimina la primera ocurrencia empezando por la izquierda de la lista del elemento indicado
lista.remove(45)
print("lista despues de remove: ", lista)
#funcion index: devuelve la posicion de la primera ocurrencia de izquierda a derecha en la lista, del elemento pasado como paralelo
print("posicion del elemento 111: ", lista.index(111))
#funcion pop:
lista.pop()
print("lista despues del pop: ", lista)
#funcion clear: elimina todos los elementos de la lista
lista.clear()
print("lista despues del clear: ", lista)
