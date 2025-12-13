soap = [
  ['S','A','P','O'],
  ['A','R','U','I'],
  ['M','E','S','A'],
  ['P','E','R','O']
]

def find_word(grid, word):
    """Find a word in the word search grid in all 8 directions."""
    rows = len(grid)
    cols = len(grid[0]) if rows > 0 else 0
    directions = [
        (0, 1),   # right
        (0, -1),  # left
        (1, 0),   # down
        (-1, 0),  # up
        (1, 1),   # diagonal down-right
        (1, -1),  # diagonal down-left
        (-1, 1),  # diagonal up-right
        (-1, -1)  # diagonal up-left
    ]
    
    def check_direction(row, col, dr, dc):
        for i, char in enumerate(word):
            r, c = row + i * dr, col + i * dc
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return False
            if grid[r][c] != char:
                return False
        return True
    
    for row in range(rows):
        for col in range(cols):
            if grid[row][col] == word[0]:
                for dr, dc in directions:
                    if check_direction(row, col, dr, dc):
                        return (row, col, dr, dc)
    return None

def print_grid(grid):
    """Print the word search grid."""
    print("\nSopa de letras:")
    print("-" * (len(grid[0]) * 2 + 1))
    for row in grid:
        print("|" + " ".join(row) + "|")
    print("-" * (len(grid[0]) * 2 + 1))

def main():
    print("=== Buscador de Palabras en Sopa de Letras ===")
    print_grid(soap)
    
    words_to_find = ["SAPO", "MESA", "PERO", "ARE", "PIO"]
    
    print("\nBuscando palabras...")
    for word in words_to_find:
        result = find_word(soap, word)
        if result:
            row, col, dr, dc = result
            direction_names = {
                (0, 1): "derecha",
                (0, -1): "izquierda", 
                (1, 0): "abajo",
                (-1, 0): "arriba",
                (1, 1): "diagonal abajo-derecha",
                (1, -1): "diagonal abajo-izquierda",
                (-1, 1): "diagonal arriba-derecha",
                (-1, -1): "diagonal arriba-izquierda"
            }
            print(f"  '{word}' encontrada en posicion ({row}, {col}) hacia {direction_names[(dr, dc)]}")
        else:
            print(f"  '{word}' no encontrada")

if __name__ == "__main__":
    main()
