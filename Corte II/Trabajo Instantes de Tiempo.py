import time           # Para medir el tiempo
import random         # Para generar números aleatorios
import matplotlib.pyplot as plt  # Para graficar

# Inicializamos listas vacías donde guardaremos los datos
tiempos = []       # Guardará los instantes de tiempo
valores = []       # Guardará los números aleatorios generados

print("Presiona Ctrl+C para detener el programa.\n")

# Registramos el tiempo inicial (inicio del programa)
t_inicio = time.time()

try:
    # Bucle infinito hasta que presiones Ctrl+C
    while True:
        # Tiempo actual desde el inicio del programa
        t_actual = time.time() - t_inicio
        
        # Generamos un número aleatorio entre 0 y 1
        num_aleatorio = random.random()
        
        # Guardamos los datos en las listas
        tiempos.append(t_actual)
        valores.append(num_aleatorio)
        
        # Mostramos el valor generado en consola
        print(f"t = {t_actual:.2f} s → número = {num_aleatorio:.4f}")
        
        # Esperamos un poco (por ejemplo, 0.1 segundos)
        time.sleep(0.1)

# Si presionas Ctrl+C, se detiene el bucle y entra al bloque except
except KeyboardInterrupt:
    print("\n\nPrograma detenido por el usuario.")
    print("Generando gráfica...")

    # Creamos la gráfica tiempo vs número aleatorio
    plt.figure(figsize=(8, 4))
    plt.plot(tiempos, valores, marker='o', linestyle='-', color='green')
    plt.title("Número aleatorio vs Tiempo")
    plt.xlabel("Tiempo (s)")
    plt.ylabel("Número aleatorio (0–1)")
    plt.grid(True)
    plt.show()
