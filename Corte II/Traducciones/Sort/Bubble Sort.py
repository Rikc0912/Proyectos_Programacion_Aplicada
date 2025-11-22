def bubble_sort(arr):
    n = len(arr)
    for i in range(n - 1):              # FOR EXTERNO
        for j in range(n - i - 1):      # FOR INTERNO
            if arr[j] > arr[j + 1]:     # CONDICIÓN DE INTERCAMBIO
                arr[j], arr[j + 1] = arr[j + 1], arr[j]  # INTERCAMBIAR

def print_array(arr):
    print(arr)

arr = [5, 1, 4, 2, 8]
print("Arreglo original:")
print_array(arr)

bubble_sort(arr)

print("Arreglo ordenado:")
print_array(arr)
