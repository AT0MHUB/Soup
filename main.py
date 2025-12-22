soup = [
  ['C','A','R','R','O'], # len(soup[0]) = 5 ene ste caso son 5 columnas
  ['A','A','R','O','S'], #len(soup) = 7 en este caso son 7 filas
  ['C','R','R','S','O'],
  ['R','O','S','A','S'],
  ['O','S','S','S','O'],
  ['S','A','S','A','S'], 
  ['C','A','R','R','O']  
]
words = ['CARRO', 'ROSAS', 'SOSA', 'COSAS', 'SARRO', 'SARSA']

def buscar_palabra(soup, words):
  rows = len(soup)
  columns = len(soup[0])
  direcciones = [[-1, 0], [1, 0], [0, 1], [0, -1],[-1, -1], [-1, 1], [1, -1], [1, 1]]
  for word in words:
    encontrada = False
    
    for row in range(rows):
      if encontrada: 
        break
        
      for col in range(columns):
        if encontrada: 
          break
          
        for df, dc in direcciones:
          found = True
          for i in range(len(word)): 
            f = row + i * df
            c = col + i * dc
            if not (0 <= f < rows and 0 <= c < columns) or \
              soup[f][c].lower() == word[i].lower():
              found = False
              break

          if found:
            print(f"La palabra {word} fue encontrada")
            encontrada = True
            break

                 
buscar_palabra(soup, words)