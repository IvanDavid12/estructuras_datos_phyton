#EJERCICIO : Los ejercicios con diccionario los hemos divivido en dos grupos diferentes.

#MANIPULACION
#

diassemanaingles = {"lunes" : "monday", "martes" : "tuesday", "miercoles" : "wednesday", "jueves" : "thursday", "viernes" : "friday"}

print(diassemanaingles["lunes"])
print(diassemanaingles["miercoles"])
print(diassemanaingles["viernes"])

#la forma de añadir elementos al diccionario
diassemanaingles["sabado"] = "saturday"
print(diassemanaingles)
#la forma de modificar el valor de un elemento del diccionario 
diassemanaingles["domingo"] = "sunday"
print(diassemanaingles)

#la forma de eliminar un elemento del diccionario 
diassemanaingles["lunes"] = "mondayBORRAR"
print(diassemanaingles)
del diassemanaingles["lunes"] 
print(diassemanaingles)
#es posible utilizar la funciones de len, max y min con los diccionarios

diassemanaingles = {"lunes" : "monday", "martes" : "tuesday", "miercoles" : "wednesday", "jueves" : "thursday", "viernes" : "friday"}

print("numero de elementos del diccionario : ", len(diassemanaingles))
print("elemento mayor del diccionario: ", max(diassemanaingles))
print("elemento mayor del diccionario: ", min(diassemanaingles))

# METODOS PROPIOS

diassemanaingles= {'Lunes': 'Monday', 'Martes': 'Tuesday','Miercoles': 'Wednesday','Jueves':'Thursday','Viernes': 'Friday'}
print('Diccionario original: ',diassemanaingles)
diccionariocopia=diassemanaingles.copy()
print('Diccionario copy: ',diccionariocopia)
print('Valor del lunes (pop): ',diassemanaingles.pop('Lunes'))
print('Diccionario despues del pop: ',diassemanaingles)
print('Elemento al azar con popitem: ',diassemanaingles.popitem())
print('Diccionario despues del popitem: ',diassemanaingles)
print('Valor del Martes (get): ',diassemanaingles.get('Martes'))
print('Valor del lunes (get) (no existe): ',diassemanaingles.get('Lunes'))
print('Valor del lunes (get) (no existe): ',diassemanaingles.get('Lunes','No existe'))
diassemanaingles.update({'Lunes':'MondayNUEVO','Martes':'Tuesday'})
print('Diccionario después del update: ',diassemanaingles)
print('setdeafult del Sábado: ',diassemanaingles.setdefault('Sabado','Saturday'))
print('Diccionario después del setdefault (nuevo elemento): ',diassemanaingles)
print('setdefault del Lunes: ',diassemanaingles.setdefault('Lunes','Lunes'))
print('Diccionario despues del setdefault (elemento existente): ',diassemanaingles)
print('Elemento iterable (items): ',diassemanaingles.items())
print('Elemento iterable (claves): ',diassemanaingles.keys())
print('Elemento iterable (valores): ',diassemanaingles.values())
print('Diccionario después del clear: ',diassemanaingles.clear())