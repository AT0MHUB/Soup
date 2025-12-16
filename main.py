soup = [
  ['C','A','R','R','O'],
  ['A','R','R','O','S'],
  ['R','R','O','S','A'],
  ['R','O','S','A','S'],
  ['O','S','A','S','A'],
  ['S','A','S','A','S'],
  ['C','A','R','R','O']
]
word = 'CARRO'

for row in range(len(soup)): # recorremos las filas
  for col in range(len(soup[row]) - len(word) + 1): # comparamos la palabra con la fila para verificar si cabe la palabra y recorremos las columnas
    found = True
    for i in range(len(word)):
      if soup[row][col + i] != word[i]:
        found = False
        break
    if found:
      print(word, "-> encontrada en la fila", row + 1, "columna", col + 1)