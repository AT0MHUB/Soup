import cv2

img = cv2.imread("sopa.png")

camino = [(0, 0), (1, 0), (2, 0), (3, 0)]
CELL = 70.5

# punto inicial
f1, c1 = camino[0]
x1 = c1 * CELL + CELL // 2
y1 = f1 * CELL + CELL // 2

# punto final
f2, c2 = camino[-1]
x2 = c2 * CELL + CELL // 2
y2 = f2 * CELL + CELL // 2

# dibujar línea
cv2.line(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

cv2.imwrite("resultado_linea.jpg", img)
print("✅ Línea dibujada en resultado_linea.jpg")
