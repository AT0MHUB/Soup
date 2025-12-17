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
for word in words:
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

