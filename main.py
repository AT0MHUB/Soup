
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
        if soup[f][c] != word[i]:
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
    soup = [
        ['C','A','R','R','0'],
        ['A','A','R','0','S'],
        ['C','R','R','S','O'],
        ['R','0','S','A','S'],
        ['O','S','5','S','O'],
        ['S','A','S','A','S'],
        ['C','A','R','R','O']
    ]

    words = ['CARRO','ROSAS','SOSA']

    soup = limpiar_sopa(soup)
    marcas = buscar_y_marcar(soup, words)
    imprimir_sopa(soup, marcas)

main()

