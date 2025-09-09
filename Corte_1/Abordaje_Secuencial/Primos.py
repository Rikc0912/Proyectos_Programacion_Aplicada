#Este Ejercicio Vale una Decima en la Calificacion del Primer Corte
#Erick Duran 20232005109
def es_primo_while(numero):
    if numero <= 1:
        return False
    if numero == 2:
        return True
    if numero % 2 == 0:
        return False
    i = 3

    while i * i <= numero:
        if numero % i == 0:
            return False  
        i += 2

    return True

while True:
    numero_a_verificar = int(input("Ingresa un número para verificar si es primo: "))

    if es_primo_while(numero_a_verificar):
        print(f"{numero_a_verificar} es un número primo.")
    else:
        print(f"{numero_a_verificar} no es un número primo.")

    continuar = input("¿Quieres verificar otro número? (s/n): ").lower()
    if continuar != 's':
        print("¡Hasta luego!")
        break