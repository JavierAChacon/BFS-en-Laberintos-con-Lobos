from collections import deque


def leerArchivo(nombre_archivo):
    with open(nombre_archivo, "r") as archivo:
        L = int(archivo.readline().strip())
        N = int(archivo.readline().strip())
        laberinto = [list(archivo.readline().strip()) for _ in range(N)]
    return L, N, laberinto


def encontrar_camino(laberinto, L, N):
    direcciones = {"N": (-1, 0), "S": (1, 0), "E": (0, 1), "O": (0, -1)}
    inicio, salida = None, None

    # Recorremos el laberinto para encontrar el punto de entrada y salida del laberinto
    for fila in range(N):
        for columna in range(N):
            if laberinto[fila][columna] == "E":
                inicio = (fila, columna)
            elif laberinto[fila][columna] == "S":
                salida = (fila, columna)

    # Validamos que haya tanto punto de entrada como de salida
    if not inicio or not salida:
        return -1, []

    # Cola para BFS (posición actual, pasos, lobos encontrados, camino)
    cola = deque([(inicio, 0, 0, [])])

    # Usamos un conjunto de tuplas (posición, lobos encontrados)
    visitado = {(inicio, 0)}

    while cola:
        (x, y), pasos, lobos, camino = cola.popleft()

        # Si llegamos a la salida, retornamos el resultado
        if (x, y) == salida:
            return pasos, camino

        # Exploramos las cuatro direcciones cardinales
        for dir in direcciones:
            dx, dy = direcciones[dir]
            nx, ny = x + dx, y + dy

            # Verificamos los límites del laberinto y si la casilla no está bloqueada
            if 0 <= nx < N and 0 <= ny < N and laberinto[nx][ny] != "#":
                # Contamos lobos si encontramos uno
                if laberinto[nx][ny] == "*":
                    nuevos_lobos = lobos + 1
                else:
                    nuevos_lobos = lobos

                # Si aún podemos enfrentar más lobos en este camino, continuamos
                if nuevos_lobos <= L and ((nx, ny), nuevos_lobos) not in visitado:
                    cola.append(((nx, ny), pasos + 1, nuevos_lobos, camino + [dir]))
                    visitado.add(((nx, ny), nuevos_lobos))

    # Si no se encontró un camino válido
    return -1, []


def escribir_salida(nombre_archivo, resultado):
    with open(nombre_archivo, "w") as archivo:
        if resultado[0] == -1:
            archivo.write("-1\n")
        else:
            archivo.write(f"Numero de pasos: {resultado[0]}\n")
            archivo.write(f"Ruta tomada: {''.join(resultado[1])}\n")


# Ejemplo de uso
L, N, laberinto = leerArchivo("laberinto.txt")

resultado = encontrar_camino(laberinto, L, N)

escribir_salida("salidalobo.txt", resultado)
