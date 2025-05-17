#Crear una función recursiva que me de la resta de la suma de los pares manos los
#impares de un lista 

def sumaresta_rec(lista, index=0, suma_pares=0, suma_impares=0):
    if index == len(lista):
        return suma_pares - suma_impares
    else:
        if lista[index] % 2 == 0:
            suma_pares += lista[index]
        else:
            suma_impares += lista[index]
        return sumaresta_rec(lista, index + 1, suma_pares, suma_impares)

# Ahora, integrando esto en tu función original:
def sumaresta():
    lista = [2, 3, 8, 1]
    return sumaresta_rec(lista)

# Llamada a la función
z = sumaresta()  # Resultado esperado: 10 - 4 = 6
print(f"Resultado: {z}")

##########################################################################################3

def sumaresta(arr, x):
    if x == 0:
        if arr[0] % 2 == 0:
            return arr[0]
        else:
            return -arr[0]
    else:
        if arr[x] % 2 == 0:
            return arr[x] + sumaresta(arr, x - 1)
        else:
            return -arr[x] + sumaresta(arr, x - 1)

# Prueba
lista = [2, 3, 8, 1]
z = sumaresta(lista, len(lista) - 1)
print(z)