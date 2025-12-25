import cv2

def preparar_imagen(ruta_imagen):
    # 1. Cargar la imagen
    imagen = cv2.imread(ruta_imagen)

    # 2. Convertir a escala de grises (eliminamos el color que no sirve)
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)

    # 3. Aplicar un desenfoque (suaviza la imagen para quitar ruido)
    desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)

    # 4. Umbral adaptativo (lo más importante)
    # Esto convierte la imagen a blanco y negro puro. 
    # Las letras se vuelven negras y el fondo blanco, sin importar las sombras.
    umbral = cv2.adaptiveThreshold(desenfoque, 255, 
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY_INV, 11, 2)

    return imagen, umbral

# Prueba esto con una foto de una sopa de letras
# original, procesada = preparar_imagen('tu_sopa.jpg')
# cv2.imshow('Procesada', procesada)
# cv2.waitKey(0)



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

   #establecemos en una lista todas las direcciones en dos dimensiones
  nombres_direcciones = {
    (-1, 0): "Vertical hacia arriba",
    (1, 0): "Vertical hacia abajo",
    (0, 1): "Horizontal a la derecha",
    (0, -1): "Horizontal a la izquierda",
    (-1, -1): "Diagonal arriba-izquierda",
    (-1, 1): "Diagonal arriba-derecha",
    (1, -1): "Diagonal abajo-izquierda",
    (1, 1): "Diagonal abajo-derecha"

  }    

   # iniciamos con esto ya que vamos a buscar varias palabras
  for word in words: 
    
    # lo indicamos en falso para que no siga buscando
    encontrada = False    

    # recorremos las filas
    for row in range(rows):
      
       #si encontramos la palabra cerramos el bucle
      if encontrada:  
        break

      #recorremos las columnas
      for col in range(columns):  
        if encontrada: 
          break

         #con esto indicamos el numero de veces que vamos a buscar en este caso 8
        for (df, dc), nombre in nombres_direcciones.items():  
          
          # hacemos como si ya la ubieramos encontrado
          found = True 
          
          # recorremos la palabra a buscar
          for i in range(len(word)):  

            # y con esto nos movemos en la sopa en este caso las filas posibles
            f = row + i * df  

            # y esta las columnas posibles
            c = col + i * dc   

            # con esto creamos un limite en el que la posicion en f y c debe ser mayor 0 igual cero y menor a las columnas y evitar errores y la segunda funcionapara comparar letra por letra
            if not (0 <= f < rows and 0 <= c < columns) or \
              soup[f][c].lower() != word[i].lower():   
              found = False
              break

          if found:
            print(f"✅ {word} encontrada: fila {row + 1}, columna {col + 1}: {nombre}")
            encontrada = True
            break

    if not encontrada:
      print(f"❌ {word} no se encontró")
buscar_palabra(soup, words)