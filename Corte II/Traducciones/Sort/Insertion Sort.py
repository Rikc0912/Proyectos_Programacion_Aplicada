def insertion_sort(arr):
    n = len(arr)
    for i in range(1, n):
        key = arr[i]      # valor que vamos a insertar
        j = i - 1

        # mover los elementos mayores que key hacia la derecha
        while j >= 0 and arr[j] > key:
            arr[j + 1] = arr[j]
            j -= 1

        # insertar la key en la posición correcta
        arr[j + 1] = key

def print_array(arr):
    print(arr)

arr = [5, 2, 4, 6, 1]
print("Arreglo original:")
print_array(arr)

insertion_sort(arr)

print("Arreglo ordenado:")
print_array(arr)
