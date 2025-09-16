Erick Duran 20232005109
#################LISTAS####################
###########################################
# Definimos una lista con varios colores
my_lista = ['Rojo', 'Azul', 'Amarillo', 'Naranja', 'Violeta', 'Verde']

# Imprimimos toda la lista
print(my_lista)

# Mostramos el tipo de dato (list)
print(type(my_lista))

# Accedemos al elemento en la posición 2 (recordemos que inicia en 0)
print(my_lista[2])

# Mostramos el tamaño (longitud) de la lista
print("my_lista size: ", len(my_lista))

# Imprimimos desde la posición 0 hasta antes de la 2 → ['Rojo', 'Azul']
print(my_lista[0:2])

# Lo mismo que arriba, omitiendo el 0 → ['Rojo', 'Azul']
print(my_lista[:2])

# Agregamos un elemento al final de la lista
my_lista.append('Blanco')
print(my_lista)

# Insertamos 'Negro' en la posición 3 (desplaza el resto)
my_lista.insert(3, 'Negro')
print(my_lista)

# Extendemos la lista concatenando otra lista con dos elementos
my_lista.extend(['Marron', 'Gris'])
print(my_lista)

# Obtenemos el índice donde aparece 'Azul'
print(my_lista.index('Azul'))

# Eliminamos el elemento 'Marron' de la lista
my_lista.remove('Marron')
print(my_lista)

# Insertamos 'Marron' en la posición 8
my_lista.insert(8, 'Marron')
print(my_lista)

# Eliminamos el último elemento de la lista y lo mostramos
print(my_lista.pop())

# Mostramos el tamaño actual de la lista
size = len(my_lista)
print("size = ", size)

# Multiplicamos la lista por 3 (se repite 3 veces)
my_lista_3 = my_lista * 3
print("my_lista_3: ", my_lista_3)

# Ordenamos la lista alfabéticamente
print("Sort:")
print()
my_listaSort = my_lista.sort()  # ¡Ojo! .sort() ordena en el lugar y devuelve None
print(my_listaSort)             # Por eso esto imprime "None"

# Lista numérica para ejemplo de ordenamiento
my_NumList = [10, 9, 8, 7, 6 , 5 , 4, 3, 2, 1]
print("Ordering my_NumList: ")

# Ordenamos de menor a mayor
my_NumList.sort()
print(my_NumList)

# Ordenamos de mayor a menor con reverse=True
my_NumList.sort(reverse = True)
print("De menor a mayor: ", my_NumList)



#################TUPLAS####################
###########################################
# Una tupla es como una lista, pero inmutable (no se puede modificar)

# Convertimos una lista a tupla
print("###########################")
print("###########################")
print("###########################")
print("############TUPLAS#########")
my_tupla = tuple(my_lista)
print()
print()
print("my_tuple: ", my_tupla)

# Accedemos a elementos de la tupla por índice
print(my_tupla[0])
print(my_tupla[2])

# Verificamos si 'Rojo' está en la tupla (True/False)
print('Rojo' in my_tupla)

# Contamos cuántas veces aparece 'Rojo'
print(my_tupla.count('Rojo'))

# Una tupla con un solo elemento → OJO: falta la coma, así no es tupla real
my_tupla_unitaria = ('Blanco')  
print(my_tupla_unitaria)  # Esto en realidad es un str

# Empaquetado de tupla: no hace falta paréntesis
my_tupla = 'Gaspar', 5, 8, 1999
print(my_tupla)

# Desempaquetado: cada valor se asigna a una variable
nombre, dia, mes, año = my_tupla
print(nombre)
print(dia)
print(mes)
print(año)

# Mostramos todas las variables desempaquetadas
print("Nombre: ", nombre, " - Dia:", dia, " - Mes: ", mes, "- Año: ", año)

# Convertimos la tupla a lista
my_lista2 = list(my_tupla)
print(my_lista2)
