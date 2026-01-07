import cv2
import pytesseract
import os

DEBUG = False

img = cv2.imread("sopa.png")
if img is None:
    print("No se cargó la imagen")
    exit()

rows = 7
cols = 7

h, w, _ = img.shape
cell_h = h // rows
cell_w = w // cols

def leer_celda(img, fila, columna, cell_h, cell_w):
    x1 = columna * cell_w
    y1 = fila * cell_h
    x2 = x1 + cell_w
    y2 = y1 + cell_h

    pad_top = 5
    pad_bottom = 2
    pad_left = 5
    pad_right = 5

    celda = img[
        y1 + pad_top : y2 - pad_bottom,
        x1 + pad_left : x2 - pad_right
    ]

    gray = cv2.cvtColor(celda, cv2.COLOR_BGR2GRAY)
    
    thresh = cv2.adaptiveThreshold(
        gray, 
        255,
        cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
        cv2.THRESH_BINARY,
        11,
        2
    )
    thresh = cv2.bitwise_not(thresh)

    texto = pytesseract.image_to_string(
        thresh,
        config="--psm 10 -c tessedit_char_whitelist=ABCDFEGHIJKLMNOPQRSTUVWXYZ"
    )
    if DEBUG: 
        os.makedirs("debug", exist_ok=True)
        cv2.imwrite(f"debug/celda_{fila}_{columna}.png", celda)
        cv2.imwrite(f"debug/celda_{fila}_{columna}.png", thresh)

    return texto.strip()



sopa_ocr = []

for fila in range(rows):
    fila_letras = []
    for columna in range(cols):
        letra = leer_celda(img, fila, columna, cell_h, cell_w)
        fila_letras.append(letra if letra else "?")
        
    sopa_ocr.append(fila_letras)

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
    reemplazos = {'0': 'O','1': 'I','5': 'S','8': 'B'}
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
        if soup[f][c].upper() != word[i].upper():
            return None
        posiciones.append((f, c))
    return posiciones

def imprimir_sopa(soup, marcas):
    print("\nSOPA\n")
    for r in range(len(soup)):
        for c in range(len(soup[0])):
            if marcas[r][c]:
                print(f"[{soup[r][c]}]", end=" ")
            else:
                print(f" {soup[r][c]} ", end=" ")
        print()

def buscar_y_marcar(soup, words):
    marcas = [[False]*len(soup[0]) for _ in soup]

    for word in words:
        for row in range(len(soup)):
            for col in range(len(soup[0])):
                for (df, dc) in DIRECTIONS:
                    pos = posiciones_palabra(soup, word, row, col, df, dc)
                    if pos:
                        for f, c in pos:
                            marcas[f][c] = True
                        break
    return marcas

def main():
    soup = sopa_ocr

    words = ["EPOCA", "falso"]

    soup = limpiar_sopa(soup)
    marcas = buscar_y_marcar(soup, words)
    imprimir_sopa(soup, marcas)


main()
