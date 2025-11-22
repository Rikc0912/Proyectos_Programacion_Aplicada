def linear_search(arr, key):
    for i in range(len(arr)):       # recorrer el arreglo
        if arr[i] == key:           # si lo encuentro
            return i                # retorno el índice
    return -1                       # no se encontró


def linear_search_all(arr, key):
    indices = []                    # lista para guardar todas las posiciones
    for i in range(len(arr)):
        if arr[i] == key:
            indices.append(i)

    return indices                  # retornamos lista (puede estar vacía)


# --- MAIN EQUIVALENTE ---
arr = [4, 9, 2, 7, 5, 7, 9, 7]
print("Arreglo:", arr)

key = int(input("Ingrese el número a buscar: "))

# --- Búsqueda de una sola posición ---
pos = linear_search(arr, key)

if pos == -1:
    print(f"El número {key} NO se encuentra en el arreglo.")
else:
    print(f"El número {key} se encuentra (al menos) en la posición {pos} (índice 0-based).")

# --- Búsqueda de todas las posiciones ---
indices = linear_search_all(arr, key)

if len(indices) == 0:
    print(f"No se encontraron ocurrencias de {key}.")
else:
    print(f"El número {key} aparece {len(indices)} veces, en las posiciones: {indices}")
