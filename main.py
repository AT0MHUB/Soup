soup = [
  ['C','A','R','R','O'], # len(soup[0]) = 5 ene ste caso son 5 columnas
  ['A','R','R','O','S'], #len(soup) = 7 en este caso son 7 filas
  ['R','R','O','S','A'],
  ['R','O','S','A','S'],
  ['O','S','A','S','A'],
  ['S','A','S','A','S'], 
  ['C','A','R','R','O']  
]
word = 'CARRO'

# busqueda horizontal
for row in range(len(soup)):                      # recorremos las filas
  for col in range(len(soup[0]) - len(word) + 1): # comparamos la palabra con la fila para verificar si cabe la palabra y recorremos las columnas
    found = True
    for i in range(len(word)):
      if soup[row][col + i] != word[i]:
        found = False
        break
    if found:
      print(f"{word} -> encontrada horizontalmente en la fila {row+1}, columna {col+1}")


# busqueda vertical
for row in range(len(soup) - len(word) + 1):     # recorremos las filas para verificar si cabe la palabra verticalmente esto tambien                                                            establece  un limite para no salirnos del rango de la matriz
  for col in range(len(soup[0])):                # recorremos las columnas
    found = True                                 # asumimos que la palabra se encuentra en la fila y columna actual
    for i in range(len(word)):                   #recorremos la palabra letra por letra
      if soup[row + i][col] != word[i]:          #comparamos la letra de la palabra con la letra de la fila y columna actual
        found = False                            # si no coinciden, la palabra no se encuentra en la fila y columna actual
        break                                    # rompemos el ciclo
    if found:                                    # si se encuentra la palabra
      print(f"{word} -> encontrada verticalmente en la fila {row+1}, columna {col+1}")

