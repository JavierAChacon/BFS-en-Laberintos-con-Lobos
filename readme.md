# Laberinto con Lobos

Seguramente ya sabes cómo encontrar el camino más corto para escapar de un laberinto, pero lamentablemente esta vez tu misión es mucho más peligrosa pues ciertos lugares de este están ocupados por lobos que intentarán comerte. Como estás en forma, crees poder enfrentarte con L lobos pero probablemente el lobo L+1 ya sea demasiado para ti. Tu labor será encontrar la ruta más corta para escapar del laberinto evitando enfrentarte con más de L lobos durante tu recorrido.

## Formato de Entrada

El archivo de texto `laberinto.txt` contendrá:
- El valor del entero L, que representa el número máximo de lobos que puedes enfrentar en tu recorrido.
- Un entero N que representa el tamaño del laberinto (N x N).
- Un tablero de N x N caracteres que representa el laberinto:
  - `E`: Entrada del laberinto.
  - `S`: Salida del laberinto.
  - `#`: Muro o pared que no se puede atravesar.
  - `*`: Lobo que debes enfrentar.
  - `.`: Espacio vacío por donde puedes moverte.

Puedes suponer que L ≥ 0, 2 ≤ N ≤ 100 y que existirán exactamente una entrada y una salida en el laberinto.

### Ejemplo de entrada:

1  
6  
####S#  
#....#  
#.##*#  
#....#  
#...*#  
####E#  

## Formato de Salida

El archivo de texto `salidalobo.txt` deberá contener:
- Un entero P que representa el número de pasos usados para salir del laberinto sin enfrentar más de L lobos, o -1 si no existe solución.
- En caso de que exista solución, el segundo renglón deberá contener la secuencia de P pasos que van desde la entrada hasta la salida, representada como una secuencia de letras `N`, `S`, `E` y `O` (Norte, Sur, Este, Oeste).

### Ejemplo de salida correspondiente al ejemplo de entrada:

Numero de pasos: 11  
Ruta tomada: NNOOONNEEEN
