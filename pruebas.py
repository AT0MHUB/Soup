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

def buscar_palabras(soup, word, dx, dy):
   rows = len(soup)   #definimos el tamaño de la sopa verticalmente
   columns = len(soup[0])  # definimos el tamaño de la sopa horizontalmente
   for row in range(rows):   #recorremos las filas
      for col in range(columns):  #recorremos las columnas
         found = True
         for i in range(len(word)): #comparamos letra por letra
            f = row + i * dx
            c = col + i * dy
            if f < 0 or f >= rows or c < 0 or c >= columns:
               found = False
               break

            if soup[f][c] != word[i]:
               found = False
               break

         if found:
            print(f"{word} encontrada en la fila {row+1}, columna {col+1} dirección ({dx},{dy}).")

buscar_palabras(soup, word, 0, 1)