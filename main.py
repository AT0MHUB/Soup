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
  rows = len(soup)  # guardamos en una variable el numero de filas de la sopa
  columns = len(soup[0]) # hacemos lo mismo con las columnas
  nombres_direcciones = {
    (-1, 0): "Vertical hacia arriba",
    (1, 0): "Vertical hacia abajo",
    (0, 1): "Horizontal a la derecha",
    (0, -1): "Horizontal a la izquierda",
    (-1, -1): "Diagonal arriba-izquierda",
    (-1, 1): "Diagonal arriba-derecha",
    (1, -1): "Diagonal abajo-izquierda",
    (1, 1): "Diagonal abajo-derecha"

  }     #establecemos en una lista todas las direcciones en dos dimensiones
  for word in words:  # iniciamos con esto ya que vamos a buscar varias palabras
    encontrada = False   # lo indicamos en falso para que no siga buscando 
    
    for row in range(rows): # recorremos las filas
      if encontrada:   #si encontramos la palabra cerramos el bucle
        break
        
      for col in range(columns):  #recorremos las columnas
        if encontrada: 
          break
          
        for (df, dc), nombre in nombres_direcciones.items():  #con esto indicamos el numero de veces que vamos a buscar en este caso 8 
          found = True  # hacemos como si ya la ubieramos encontrado
          for i in range(len(word)):  # recorremos la palabra a buscar
            f = row + i * df   # y con esto nos movemos en la sopa en este caso las filas posibles 
            c = col + i * dc   # y esta las columnas posibles
            if not (0 <= f < rows and 0 <= c < columns) or \
              soup[f][c].lower() != word[i].lower():   # con esto creamos un limite en el que la posicion en f y c debe ser mayor 0 igual cero y menor a las columnas y evitar errores y la segunda funcionapara comparar letra por letra
              found = False
              break

          if found:
            print(f"✅ {word} encontrada: fila {row + 1}, columna {col + 1}: {nombre}")
            encontrada = True
            break

    if not encontrada:
      print(f"❌ {word} no se encontró")
buscar_palabra(soup, words)