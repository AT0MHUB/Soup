soup = [
  ['C','A','R','R','O'], # len(soup[0]) = 5 ene ste caso son 5 columnas
  ['A','A','R','O','S'], #len(soup) = 7 en este caso son 7 filas
  ['C','R','R','S','O'],
  ['R','O','S','A','S'],
  ['O','S','S','S','O'],
  ['S','A','S','A','S'], 
  ['C','A','R','R','O']  
]

words = ['ORRAC','CASA','CARRO','ROSAS','SOSA','COSAS','SARRO','SARSA','SAROS','SARRO','SARSA','SAROS','SARRO']
word = 'CARRO'

derecha = 0, 1
izquierda = 0, -1
abajo = 1, 0
arriba = -1, 0
diagonal_abajo_derecha = 1, 1
diagonal_arriba_izquierda = -1, -1
diagonal_arriba_derecha = -1, 1
diagonal_abajo_izquierda = 1, -1

dx = [0, 0, 1, -1, 1, -1, -1, 1]
dy = [1, -1, 0, 0, 1, -1, 1, -1]

# Lista de pares [dx, dy] para las 8 direcciones
direcciones = [
    [-1, 0], [1, 0], [0, 1], [0, -1], # Ortogonales
    [-1, -1], [-1, 1], [1, -1], [1, 1] # Diagonales
]

def buscar_palabra(soup, word):
   direcciones = [[-1, 0], [1, 0], [0, 1], [0, -1],[-1, -1], [-1, 1], [1, -1], [1, 1]]
   rows = len(soup)
   columns = len(soup[0])
   for row in range(rows):
      for col in range(columns):
         for df, dc in direcciones:
            for i in range(len(word)): 
               f = row + i * df
               c = col + i * dc
               if 0 <= f < rows and 0 <= c < columns:
                  if soup[f][c].lower() == word[i].lower():
                     return print(f"la palabra {word} fue encontrada en la fila {row + 1}")
                  else:
                     break
               else:
                  break
buscar_palabra(soup,"CARRo")
   
# busqueda horizontal
for word in words:
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

  #busqueda diagonal
  for row in range(len(soup) - len(word) + 1):     # recorremos las filas para verificar si cabe la palabra diagonalmente esto tambien                                                            establece  un limite para no salirnos del rango de la matriz
     for col in range(len(soup[0]) - len(word) + 1): # comparamos la palabra con la fila para verificar si cabe la palabra diagonalmente
        found = True
        for i in range(len(word)):
           if soup[row + i][col + i] != word[i]:  # comparamos la letra de la palabra con la letra de la fila y columna actual
              found = False
              break
        if found:
           print(f"{word} -> encontrada diagonalmente en la fila {row+1}, columna {col+1}")

  #busqueda horizontal invertida

  for row in range(len(soup)):                                    # recorremos las filas
    for col in range(len(word) - 1, len(soup[0])): # comparamos la palabra con la fila de derecha a izquierda
      found = True
      for i in range(len(word)):
        if soup[row][col - i] != word[i]:
          found = False
          break
      if found:
        print(f"{word} -> encontrada horizontalmente invertida en la fila {row+1}, columna {col+1}")

  #busqueda vertical invertida
  for row in range(len(word) - 1, len(soup)): # recorremos las filas de abajo hacia arriba
     for col in range(len(soup[0])):                      # recorremos las columnas
        found = True
        for i in range(len(word)):
           if soup[row - i][col] != word[i]:
              found = False
              break
        if found:
           print(f"{word} -> encontrada verticalmente invertida en la fila {row+1}, columna {col+1}")

  #busqueda diagonal invertida
  for row in range(len(word) - 1, len(soup)): # recorremos las filas de abajo hacia arriba diagonalmente
       for col in range(len(word) - 1, len(soup[0])): # recorremos las columnas de derecha a izquierda  diagonalmente
          found = True
          for i in range(len(word)):
             if soup[row - i][col - i] != word[i]:
                found = False
                break
          if found:
             print(f"{word} -> encontrada diagonalmente invertida en la fila {row+1}, columna {col+1}")

