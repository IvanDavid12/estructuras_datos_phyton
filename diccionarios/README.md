# DICCIONARIOS

En este apartado vamos a hablar sobre los tipos de datos diccionarios, que son un conjunto ordenado de elementos cuyos indices no son numericos si no datos de cualquier tipo. En otras oalabras, los diccionarios son colecciones de elementos compuestos por una clave y un valor asociado, con la caracteristica de que las claves no pudden repetirse. 

Los diccionarios de python se delimitan por corchetes "{ }", con los elementos separados por comas y la clave separada del valor mediante dos puntos veamos un ejemplo de diccionario 

`{"clave1":"valor1","clave2":"valor2","vlave3:"valor3"}`

El diccionario de ejmplos estan compuesto por tres elementos, en la siguiente tabla te mostramos la relacion entre la clave y el valor asociado 

|clave|valor|
|-----|-----|
|"clave1|"valor1"|
|"clave2|"valor2"|
|"clave3|"valor3"|

Las claves de los diccionarios pueden ser de diferentes tipos de datos, aunque siempre debera de ser datos inmutables. los tipos de datos soportados en python para se claves de los diccionarios son

° cadena de texto (str)
° numeros(enteros,reales y complejos)
° booleanos
° bytes
° tupla

Aunque puedes utilizar todos ellos como clave, lo mas comunes son cadenas de texto y enteros

# MANIPULACION 

en este apartado vamos a utilizar para manipular los elementos del diccionario 

# METODOS PROPIOS

el tipo de datos diccionario en python posee una serie de funciones que nos permiten manipular los diccionarios realizando operaciones complejas de forma sencilla y con una simple instruccion el formato de uso de la gran mayoria de las funciones es la siguiente 

`diccionario.nombrefuncion(parametros)`

veamos en detalles cada una de las partes

°diccionario: diccionario que ejecuta la funcion 
°nombrefuncion: nombre de la funcion que se quiere ejecutar
°parametros: no todas las funciones tienen parametros para ejecutarse, esta parte es dependiente de las funciones que se quieren ejecutar

la funciones de lista que ponen a nuestra disposicion python son las siguientes

°copy: realiza una copia exacta del diccionario en uno nuevo
-valor devuelto: diccionario copiado
-parametro: no tiene

°pop: obtiene el valor de la clave pasada como parametro y ademas elimina el elemento del diccionario
-valor devuelto: valor del elemento o error en caso de no encontrar la clave en el diccionario
-parametros: clave a buscar en el diccionario

°popitem: obtiene un elemento aleatorio del diccionario y lo elimina del mismo
-valor devuelto: ddevolvera el valor del elemento en caso de existir dicha clave y en caso de no existir devolvera "none". Existe la posibilidad de especificar mediante un segundo parametro un valor diferente a "none" como retorno 
-parametro: tiene dos parametros el primero es obligatorio y es la clave del elemento buscar y el segundo es opcional y es el valor que quiere retornar

