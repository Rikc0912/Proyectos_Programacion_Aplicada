def merge(arr, l, m, r):
    # Subarreglos temporales
    L = arr[l:m + 1]
    R = arr[m + 1:r + 1]

    i = j = 0
    k = l

    # Mezclar L y R
    while i < len(L) and j < len(R):
        if L[i] <= R[j]:
            arr[k] = L[i]
            i += 1
        else:
            arr[k] = R[j]
            j += 1
        k += 1

    # Copiar lo que queda de L
    while i < len(L):
        arr[k] = L[i]
        i += 1
        k += 1

    # Copiar lo que queda de R
    while j < len(R):
        arr[k] = R[j]
        j += 1
        k += 1


def merge_sort(arr, l, r):
    if l < r:
        m = (l + r) // 2
        merge_sort(arr, l, m)      # izquierda
        merge_sort(arr, m + 1, r)  # derecha
        merge(arr, l, m, r)        # mezclar


arr = [10, 7, 8, 9, 1, 5]
merge_sort(arr, 0, len(arr) - 1)

print("Arreglo ordenado:")
print(arr)
