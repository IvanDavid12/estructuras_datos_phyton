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
#5. uso del operador *, permite concantear una lista con ella misma un numero finito de veces
lista1=["camiseta", "pantalon", "zapatillas"]
print(lista)
lista_resultado = lista * 3
print(lista_resultado)

#6. creacion de listas como elemento listas y accesos a dichos elementos
lista1=["camiseta", "pantalon", "cazadores", "zapatillas"]
print(lista)
print(lista[0])
print(lista[1])
print(lista[2])
print(lista[1] [0])
print(lista[1] [1])

# 7. extraer una porcion de la lista en una lista nueva
lista = [1, 2, 3, 4, 5, 6, 7, 8, 9]
print(lista)
lista = lista [3:7]
print(lista)
lista2 = (lista[:5])
print(lista2)
lista3 = lista[3:]
print(lista3)