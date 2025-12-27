import cv2
import pytesseract
from PIL import Image
import os

DIRECTIONS = {
    (0, 1): "derecha",
    (0, -1): "izquierda",
    (1, 0): "abajo",
    (-1, 0): "arriba",
    (1, 1): "diagonal abajo-derecha",
    (-1, -1): "diagonal arriba-izquierda",
    (1, -1): "diagonal abajo-izquierda",
    (-1, 1): "diagonal arriba-derecha"
}


def procesar_imagen(ruta_imagen):
    """Carga una imagen y extrae el texto usando OCR"""
    print(f"Cargando imagen: {ruta_imagen}")
    
    # Leer la imagen
    imagen = cv2.imread(ruta_imagen)
    
    if imagen is None:
        print(f"❌ No se pudo cargar la imagen: {ruta_imagen}")
        return None
    
    # Convertir a escala de grises
    gris = cv2.cvtColor(imagen, cv2.COLOR_BGR2GRAY)
    
    # Aplicar desenfoque para reducir ruido
    desenfoque = cv2.GaussianBlur(gris, (5, 5), 0)
    
    # Aplicar umbral adaptativo para mejorar contraste
    umbral = cv2.adaptiveThreshold(desenfoque, 255, 
                                   cv2.ADAPTIVE_THRESH_GAUSSIAN_C, 
                                   cv2.THRESH_BINARY, 11, 2)
    
    # Usar OCR para extraer texto
    print("Extrayendo texto con OCR...")
    texto = pytesseract.image_to_string(umbral, lang='spa')
    
    return texto


def texto_a_sopa(texto):
    """Convierte el texto extraído en una matriz de caracteres"""
    lineas = texto.strip().split('\n')
    sopa = []
    
    for linea in lineas:
        # Limpiar espacios y convertir a mayúsculas
        caracteres = [c.upper() for c in linea if c.isalpha() or c.isdigit()]
        if caracteres:
            sopa.append(caracteres)
    
    return sopa


def limpiar_letra(letra):
    reemplazos = {'0': 'O', '1': 'I', '5': 'S', '8': 'B'}
    letra = letra.upper()
    if letra in reemplazos:
        return reemplazos[letra]
    if not letra.isalpha():
        return None
    return letra


def limpiar_sopa(soup):
    soup_limpia = []
    for fila in soup:
        nueva_fila = []
        for letra in fila:
            limpia = limpiar_letra(letra)
            nueva_fila.append(limpia if limpia else '?')
        soup_limpia.append(nueva_fila)
    return soup_limpia


def posiciones_palabra(soup, word, row, col, df, dc):
    posiciones = []
    for i in range(len(word)):
        f = row + i * df
        c = col + i * dc
        if not (0 <= f < len(soup) and 0 <= c < len(soup[0])):
            return None
        if soup[f][c] != word[i]:
            return None
        posiciones.append((f, c))
    return posiciones


def imprimir_sopa(soup, marcas):
    print("\n" + "="*50)
    print("SOPA DE LETRAS")
    print("="*50 + "\n")
    for r in range(len(soup)):
        for c in range(len(soup[0])):
            if marcas[r][c]:
                print(f"[{soup[r][c]}]", end=" ")
            else:
                print(f" {soup[r][c]} ", end=" ")
        print()
    print()


def buscar_y_marcar(soup, words):
    marcas = [[False]*len(soup[0]) for _ in soup]

    for word in words:
        encontrada = False
        for row in range(len(soup)):
            if encontrada:
                break
            for col in range(len(soup[0])):
                if encontrada:
                    break
                for (df, dc) in DIRECTIONS:
                    pos = posiciones_palabra(soup, word, row, col, df, dc)
                    if pos:
                        for f, c in pos:
                            marcas[f][c] = True
                        print(f"✅ {word} encontrada en: fila {row+1}, columna {col+1}")
                        encontrada = True
                        break
        if not encontrada:
            print(f"❌ {word} no se encontró")
    
    return marcas


def main():
    print("\n" + "="*50)
    print("BÚSQUEDA DE PALABRAS EN SOPA DE LETRAS")
    print("="*50 + "\n")
    
    # Opción 1: Usar una imagen
    ruta_imagen = "sopa.png"
    
    if os.path.exists(ruta_imagen):
        print(f"Imagen encontrada: {ruta_imagen}")
        texto = procesar_imagen(ruta_imagen)
        
        if texto:
            print(f"\nTexto extraído:\n{texto}\n")
            soup = texto_a_sopa(texto)
            
            if soup:
                # Pedir las palabras a buscar
                print("Ingresa las palabras a buscar (separadas por comas):")
                palabras_input = input().strip()
                palabras = [p.strip().upper() for p in palabras_input.split(',')]
                
                soup = limpiar_sopa(soup)
                marcas = buscar_y_marcar(soup, palabras)
                imprimir_sopa(soup, marcas)
            else:
                print("❌ No se pudo extraer texto de la imagen")
    else:
        # Opción 2: Usar datos de prueba
        print("No se encontró imagen. Usando datos de prueba...\n")
        
        soup = [
            ['C','A','R','R','O'],
            ['A','A','R','O','S'],
            ['C','R','R','S','O'],
            ['R','O','S','A','S'],
            ['O','S','S','S','O'],
            ['S','A','S','A','S'],
            ['C','A','R','R','O']
        ]
        
        palabras = ['CARRO', 'ROSAS', 'SOSA', 'COSAS', 'SARRO', 'SARSA']
        
        soup = limpiar_sopa(soup)
        marcas = buscar_y_marcar(soup, palabras)
        imprimir_sopa(soup, marcas)
        
        print("\n💡 Para usar una imagen:")
        print("   1. Sube una imagen llamada 'sopa.png' a tu proyecto")
        print("   2. Ejecuta este programa de nuevo")


if __name__ == "__main__":
    main()
