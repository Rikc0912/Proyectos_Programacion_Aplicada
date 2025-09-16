#### Diccionarios en Python ####

# Crear un diccionario con edificios y su altura
building_heights = {"Burj Khalifa": 828, "Shanghai Tower": 632, 
                    "Abraj Al Bait": 601, "Ping An": 599, 
                    "Lotte World Tower": 554.5, "One World Trade": 541.3}

# Acceder a los valores usando la clave
print(building_heights["Burj Khalifa"])  # Imprime 828
print(building_heights["Ping An"])       # Imprime 599


# Diccionario con listas como valores
zodiac_elements = {"water": ["Cancer", "Scorpio", "Pisces"],
                   "fire": ["Aries", "Leo", "Sagittarius"],
                   "earth": ["Taurus", "Virgo", "Capricorn"],
                   "air": ["Gemini", "Libra", "Aquarius"]}

print(zodiac_elements["earth"])  # Imprime la lista de signos de tierra
print(zodiac_elements["fire"])   # Imprime la lista de signos de fuego


# Acceder a una clave que no existe lanza error
# print(building_heights["Landmark 81"])  # KeyError


# Para evitar error, se puede comprobar primero
key_to_check = "Landmark 81"
if key_to_check in building_heights:
    print(building_heights["Landmark 81"])


# Se puede añadir un nuevo par clave-valor
zodiac_elements["energy"] = "Not a Zodiac element"
if "energy" in zodiac_elements:
    print(zodiac_elements["energy"])  # Imprime el valor agregado


# Usar .get() para acceder de forma segura
print(building_heights.get("Shanghai Tower"))  # Devuelve 632
print(building_heights.get("My House"))        # Devuelve None


# Diccionario con IDs de usuario
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 102931, 
            "keysmithKeith": 129384}

# Obtener valor con .get()
print(user_ids.get("teraCoder"))  # Devuelve 100019

# Manejo con condicionales para asignar un valor por defecto
if user_ids.get("teraCoder") == None:
    tc_id = 1000
else:
    tc_id = user_ids.get("teraCoder")
print(tc_id)  # Imprime 100019

if user_ids.get("superStackSmash") == None:
    stack_id = 100000
print(stack_id)  # Imprime 100000


# Eliminar elementos con .pop()
raffle = {223842: "Teddy Bear", 872921: "Concert Tickets", 
          320291: "Gift Basket", 412123: "Necklace", 
          298787: "Pasta Maker"}

print(raffle.pop(320291, "No Prize"))  # Elimina y devuelve "Gift Basket"
print(raffle)

print(raffle.pop(100000, "No Prize"))  # Como no existe, devuelve "No Prize"
print(raffle)

print(raffle.pop(872921, "No Prize"))  # Elimina y devuelve "Concert Tickets"
print(raffle)


# Ejemplo con juego de objetos
available_items = {"health potion": 10, "cake of the cure": 5, 
                   "green elixir": 20, "strength sandwich": 25, 
                   "stamina grains": 15, "power stew": 30}
health_points = 20

# Sumar al puntaje y eliminar claves si existen
health_points += available_items.pop("stamina grains", 0)
health_points += available_items.pop("power stew", 0)
health_points += available_items.pop("mystic bread", 0)

print(available_items)   # Se eliminaron los objetos usados
print(health_points)     # Salud final


# Obtener todas las claves
test_scores = {"Grace":[80, 72, 90], "Jeffrey":[88, 68, 81], 
               "Sylvia":[80, 82, 84], "Pedro":[98, 96, 95], 
               "Martin":[78, 80, 78], "Dina":[64, 60, 75]}

print(list(test_scores))  # Convierte claves en lista
for student in test_scores.keys():
    print(student)        # Imprime cada nombre


# Obtener claves de distintos diccionarios
user_ids = {"teraCoder": 100019, "pythonGuy": 182921, 
            "samTheJavaMaam": 123112, "lyleLoop": 102931, 
            "keysmithKeith": 129384}
num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, 
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

users = user_ids.keys()
lessons = num_exercises.keys()

print(users)
print(lessons)


# Obtener todos los valores
for score_list in test_scores.values():
    print(score_list)  # Imprime listas de notas

num_exercises = {"functions": 10, "syntax": 13, "control flow": 15, 
                 "loops": 22, "lists": 19, "classes": 18, "dictionaries": 18}

total_exercises = 0
for exercises in num_exercises.values():
    total_exercises += exercises
print(total_exercises)  # Suma total de ejercicios


# Obtener todos los pares clave-valor
biggest_brands = {"Apple": 184, "Google": 141.7, "Microsoft": 80, 
                  "Coca-Cola": 69.7, "Amazon": 64.8}

for company, value in biggest_brands.items():
    print(company + " has a value of " + str(value) + " billion dollars.")


# Ejemplo con porcentajes
pct_women_in_occupation = {"CEO": 28, "Engineering Manager": 9, 
                           "Pharmacist": 58, "Physician": 40, 
                           "Lawyer": 37, "Aerospace Engineer": 9}

for occupation, percentage in pct_women_in_occupation.items():
    print("Women make up " + str(percentage) + " percent of " + occupation + "s.")
