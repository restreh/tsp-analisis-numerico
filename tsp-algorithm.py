import numpy as np
import matplotlib.pyplot as plt
import random
import math

def leer_coordenadas(archivo):
    with open(archivo, 'r') as f:
        coordenadas = [list(map(float, line.strip().split())) for line in f]
    return coordenadas


def leer_matriz_distancias(archivo):
    with open(archivo, 'r') as f:
        matriz = [list(map(float, line.strip().split())) for line in f]
    return matriz


def calcular_distancia_total(recorrido, matriz_distancias):
    return sum(matriz_distancias[recorrido[i]][recorrido[i + 1]] for i in range(len(recorrido) - 1))

def recocido_simulado(matriz_distancias, coordenadas):
    n = len(matriz_distancias)
    recorrido = list(range(n))
    random.shuffle(recorrido)
    recorrido.append(recorrido[0])
    distancia_actual = calcular_distancia_total(recorrido, matriz_distancias)

    T = 100.0
    T_min = 1e-3
    alpha = 0.995

    while T > T_min:
        i, j = sorted(random.sample(range(1, n), 2))
        nuevo_recorrido = recorrido[:i] + recorrido[i:j][::-1] + recorrido[j:]
        nueva_distancia = calcular_distancia_total(nuevo_recorrido, matriz_distancias)

        if nueva_distancia < distancia_actual or random.random() < math.exp((distancia_actual - nueva_distancia) / T):
            recorrido = nuevo_recorrido
            distancia_actual = nueva_distancia

        T *= alpha

    return recorrido, distancia_actual


def graficar_recorrido(recorrido, coordenadas):
    x = [coordenadas[i][0] for i in recorrido]
    y = [coordenadas[i][1] for i in recorrido]

    plt.figure(figsize=(10, 5))
    plt.plot(x, y, 'o-', color='blue')
    plt.title('Recorrido óptimo aproximado (TSP)')
    plt.xlabel('X')
    plt.ylabel('Y')
    for i, txt in enumerate(recorrido):
        plt.annotate(txt, (x[i], y[i]))
    plt.show()


def main():
    archivo_coordenadas = 'Coord3.txt'
    archivo_matriz_distancias = 'Dist3.txt'

    coordenadas = leer_coordenadas(archivo_coordenadas)
    matriz_distancias = leer_matriz_distancias(archivo_matriz_distancias)

    recorrido, distancia = recocido_simulado(matriz_distancias, coordenadas)
    print(f'Recorrido óptimo aproximado: {recorrido}')
    print(f'Distancia total: {distancia:.2f}')

    graficar_recorrido(recorrido, coordenadas)

if __name__ == '__main__':
    main()
