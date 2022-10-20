# ejercicio listas

# ejercicio maniṕulacion


# 1. consistste en la manipulacion de un alista con el elementos de diferente tipo y en mostrarla por la pantalla, tanto entera como por elemento accediente a la pocsicion que ocupa dentro de la lista
lista=["python", "guanenta", 2022, "libro", 3]
print(lista)
print(lista[0])
print(lista[2])

# 2. consiste en el uso del operador + para realizar uniones de listas
lista1=["camiseta", "pantalon", "zapatillas"]
lista2=["abrigo", "jersey", "sudadera", "calcetines"]
print("numero elemento lista: ", len(lista1))
print("lista1: ", lista1)
print("numero elemento lista: ", len(lista2))
print("lista2: ", lista2)
lista_concretada = lista1 + lista2
print("numero elementos lista_concantenada: ", len(lista_concantenada))
print("lista concantenada: ", lista_concantenada)

# 3. añadir elementos a la lista de diferente formas

lista1=["camiseta", "pantalon", "zapatillas"]
print(lista)
lista = lista + ["abrigo"]
lista = lista + ["jersey", "sudadera"]
print(lista)
lista = lista + ["calcentines"] + ["bufanda"]

# 4. modificar elementos de una lista y borrar elementos de la misma
lista1=["camiseta", "pantalon", "zapatillas"]
print(lista)
lista[1] = ("cazadora")
print(lista)
del lista[0]
print(lista)
