#----------"TUPLA"----------
# ejemplos

tupla = ("casa", "2", 345, "perro", 99)
print("elementos de la tupla: ", tupla)
print("elementos de la posicion 0 ", tupla[0])
print("elementos de la posicion 1 ", tupla[1])
print("elementos de la posicion 2 ", tupla[2])
print("elementos de la posicion 3 ", tupla[3])
print("elementos de la posicion 4 ", tupla[4])

# 1. tuplas [n:m] la instruccion extraera una nueva tupla que empezara en el indice n y terminara en el m-1. Tienes que tener en cuenta los siguiente
#-n siempre tiene que ser menor que m 
#-si no se especifica el valor para n se supone que es 0
#-si no se especifica valor m se supone que es el tamaño dde la lista menos uno

tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9)
print(tupla)
print(tupla[4:9])
print(tupla[:3])
print(tupla[2:])
#2. tupla concatenada = tupla1 + tupla2 : ademas vamos a aprender  utilizar una funcion para conocer el numero de elementos que compone la tupla, dicha funcion se llama len y devuelve un entero que indica el numer de elementos que la componen se utiliza de la siguente manera
numeroElementos = len(tupla)
tupla1 = (29, "televicion", 8763)
tupla2 = (1, 2, 3, "videojuegos")
print("numero de tupla1 : ", len(tupla1))
print("tupla1: ", tupla1)
print("numero de tupla2 : ", len(tupla2))
print("tupla2: ", tupla2)
tuplaconcatenada = tupla1 + tupla2
print("numero de elementos de tuplaconcatenada : ", len(tuplaconcatenada))
print("tuplaconcatenada: ", tuplaconcatenada)

#3. tuplaresultante = tupla * numero entero: la tupla resultante de la multiplicacion sera una tupla compuesta por tantas veces la tupla como valor tenga el numero entero
tupla = (1, 2, 3, 4, 5, 6, 7, 8, 9, 0)
print(tupla)
tuplaresultante = tupla * 4
print(tuplaresultante)
