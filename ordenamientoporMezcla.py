def merge_sort(arr):
    if len(arr) <= 1:
        return arr
    
    # Dividir el array en dos mitades
    mid = len(arr) // 2
    left_half = arr[:mid]
    right_half = arr[mid:]
    
    # Llamada recursiva para ordenar cada mitad
    left_sorted = merge_sort(left_half)
    right_sorted = merge_sort(right_half)
    
    # Combinar las mitades ordenadas
    return merge(left_sorted, right_sorted)

def merge(left, right):
    merged = []
    left_idx, right_idx = 0, 0
    
    # Comparar elementos y agregar el menor
    while left_idx < len(left) and right_idx < len(right):
        if left[left_idx] < right[right_idx]:
            merged.append(left[left_idx])
            left_idx += 1
        else:
            merged.append(right[right_idx])
            right_idx += 1
    
    # Agregar los elementos restantes (si los hay)
    merged.extend(left[left_idx:])
    merged.extend(right[right_idx:])
    
    return merged

# Ejemplo de uso
if __name__ == "__main__":
    arr = [38, 27, 43, 3, 9, 82, 10]
    print("Array original:", arr)
    sorted_arr = merge_sort(arr)
    print("Array ordenado:", sorted_arr)