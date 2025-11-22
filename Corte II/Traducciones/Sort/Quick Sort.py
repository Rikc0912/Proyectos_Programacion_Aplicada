def swap(arr, i, j):
    arr[i], arr[j] = arr[j], arr[i]

def partition(arr, low, high):
    pivot = arr[high]   # último elemento como pivote
    i = low - 1

    for j in range(low, high):
        if arr[j] < pivot:
            i += 1
            swap(arr, i, j)

    swap(arr, i + 1, high)
    return i + 1  # nueva posición del pivote

def quick_sort(arr, low, high):
    if low < high:
        pi = partition(arr, low, high)
        quick_sort(arr, low, pi - 1)   # izquierda
        quick_sort(arr, pi + 1, high)  # derecha

def print_array(arr):
    print(arr)

arr = [10, 7, 8, 9, 1, 5]
print("Arreglo original:")
print_array(arr)

quick_sort(arr, 0, len(arr) - 1)

print("Arreglo ordenado:")
print_array(arr)
