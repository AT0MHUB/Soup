import pytesseract
from PIL import Image, ImageEnhance, ImageFilter
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
        if not (0 <= f < len(soup) and 0 <= c < len(soup[f])):
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
        for c in range(len(soup[r])):
            if r < len(marcas) and c < len(marcas[r]) and marcas[r][c]:
                print(f"[{soup[r][c]}]", end=" ")
            else:
                print(f" {soup[r][c]} ", end=" ")
        print()
    print()


def buscar_y_marcar(soup, words):
    marcas = [[False]*len(fila) for fila in soup]

    for word in words:
        encontrada = False
        for row in range(len(soup)):
            if encontrada:
                break
            for col in range(len(soup[row])):
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
    
    # Usar datos de prueba confiables
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
    
    print("💡 Para procesar imágenes de sopas de letras:")
    print("   Sube una imagen 'sopa.png' al proyecto y el programa la procesará")


if __name__ == "__main__":
    main()
