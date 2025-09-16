# Definimos un diccionario con sensores y temperaturas por habitación
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20, "pantry": 22}

# Definimos un diccionario con número de cámaras por lugar
num_cameras = {"backyard": 6, "garage": 2, "driveway": 1}

# Imprimimos los diccionarios
print(sensors)
print(num_cameras)

# Diccionario de traducciones
translations = {"mountain": "orod", "bread": "bass", "friend": "mellon", "horse": "roch"}
print(translations)

# ❌ ERROR: no se puede usar una lista como clave (porque no es inmutable)
# powers = {[1, 2, 4, 8, 16]: 2, [1, 3, 9, 27, 81]: 3}

# Diccionario con listas como valores (válido porque las listas son mutables)
children = {"von Trapp": ["Johannes", "Rosmarie", "Eleonore"],
            "Corleone": ["Sonny", "Fredo", "Michael"]}
print(children)

# Diccionario vacío
my_empty_dictionary = {}
print(my_empty_dictionary)

# Diccionario de menú con precios
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Agregamos un nuevo elemento usando sintaxis de clave
menu["cheesecake"] = 8
print("After", menu)

# Crear un diccionario nuevo (reemplaza al anterior con la última asignación)
animals_in_zoo = {"dinosaurs": 0}
animals_in_zoo = {"horses": 2}
print(animals_in_zoo)


## 🔹 Agregar múltiples claves con update()
sensors = {"living room": 21, "kitchen": 23, "bedroom": 20}
print("Before", sensors)

# Con update() añadimos varias entradas a la vez
sensors.update({"pantry": 22, "guest room": 25, "patio": 34})
print("After", sensors)

# Otro ejemplo: actualizar diccionario de usuarios
user_ids = {"teraCoder": 9018293, "proProgrammer": 119238}
print(user_ids)

# Agregamos más usuarios
user_ids.update({"theLooper": 138475, "stringQueen": 85739})
print(user_ids)


## 🔹 Sobrescribir valores
menu = {"oatmeal": 3, "avocado toast": 6, "carrot juice": 5, "blueberry muffin": 2}
print("Before: ", menu)

# Cambiamos el valor de "oatmeal" de 3 a 5
menu["oatmeal"] = 5
print("After", menu)

# Otro ejemplo: actualizar un diccionario de premios
oscar_winners = {"Best Picture": "La La Land", "Best Actor": "Casey Affleck",
                 "Best Actress": "Emma Stone", "Animated Feature": "Zootopia"}
print("Before", oscar_winners)
print()

# Agregamos nueva clave "Supporting Actress"
oscar_winners.update({"Supporting Actress": "Viola Davis"})
print("After1", oscar_winners)
print()

# Cambiamos el valor de "Best Picture" a "Moonlight"
oscar_winners["Best Picture"] = "Moonlight"
print("After2", oscar_winners)


### 🔹 Dict Comprehensions
# Dos listas: nombres y alturas
names = ['Jenny', 'Alexus', 'Sam', 'Grace']
heights = [61, 70, 67, 64]

# zip() combina los elementos en pares (tuplas)
zipStudents = zip(names, heights)
print("zipStudents: ", zipStudents)  # Es un objeto zip (iterador)

# Creamos un diccionario con comprensión a partir de zip
students = {key: value for key, value in zip(names, heights)}
# Resultado: {'Jenny': 61, 'Alexus': 70, 'Sam': 67, 'Grace': 64}
print(students)

# Otro ejemplo: bebidas con cafeína
drinks = ["espresso", "chai", "decaf", "drip"]
caffeine = [64, 40, 0, 120]

# zip() genera pares bebida-cafeína
zipped_drinks = zip(drinks, caffeine)
print(zipped_drinks)

# Creamos un diccionario usando comprensión
drinks_to_caffeine = {key: value for key, value in zipped_drinks}
print(drinks_to_caffeine)


### 🔹 Ejemplo de biblioteca musical
songs = ["Like a Rolling Stone", "Satisfaction", "Imagine",
         "What's Going On", "Respect", "Good Vibrations"]
playcounts = [78, 29, 44, 21, 89, 5]

# Creamos un diccionario {canción: número de reproducciones}
plays = {key: value for key, value in zip(songs, playcounts)}
print(plays)

# Agregamos una nueva canción con update()
plays.update({"Purple Haze": 1})

# Sobrescribimos el valor de "Respect" (antes 89, ahora 94)
plays.update({"Respect": 94})
print("After: ", plays)

# Creamos un diccionario anidado para representar bibliotecas de playlists
library = {"The Best Songs": plays, "Sunday Feelings": {}}
print(library)
