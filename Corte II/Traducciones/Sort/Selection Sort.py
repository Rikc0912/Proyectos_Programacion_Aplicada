def selection_sort(arr):
    n = len(arr)
    for i in range(n - 1):
        min_index = i  # asumimos que el menor está en i

        # buscar el menor
        for j in range(i + 1, n):
            if arr[j] < arr[min_index]:
                min_index = j

        # intercambiar si encontramos un menor
        if min_index != i:
            arr[i], arr[min_index] = arr[min_index], arr[i]

def print_array(arr):
    print(arr)

arr = [5, 3, 6, 1, 4]
print("Arreglo original:")
print_array(arr)

selection_sort(arr)

print("Arreglo ordenado:")
print_array(arr)
