import cv2
import pytesseract

img = cv2.imread("sopa.png")

if img is None:
  print("No se cargó la imagen")
  exit()

print("Imagen cargada ")
print(img.shape)

rows = 7
cols = 7

h, w, _ = img.shape

cell_h = h // rows
cell_w = w // cols


print(cell_h, cell_w)

for r in range(rows):
  for c in range(cols):
      x1 = c * cell_w
      y1 = r * cell_h
      x2 = x1 + cell_w
      y2 = y1 + cell_h

      cv2.rectangle(img, (x1, y1), (x2, y2), (0, 255, 0), 1)

fila = 0     #fila -> eje Y
columna = 6  #columna -> eje X

x1 = columna * cell_w
y1 = fila * cell_h

x2 = x1 + cell_w
y2 = y1 + cell_h

cv2.rectangle(img, (x1, y1), (x2, y2), (0, 0, 255), 3)

pad_top = 5
pad_bottom = 2
pad_left = 5
pad_right = 5

celda = img[
    y1 + pad_top : y2 - pad_bottom,
    x1 + pad_left : x2 - pad_right
]


gray = cv2.cvtColor(celda, cv2.COLOR_BGR2GRAY)
_, thresh = cv2.threshold(gray, 150, 255, cv2.THRESH_BINARY)

texto = pytesseract.image_to_string(
  thresh,
  config="--psm 10 -c tessedit_char_whitelist=ABCDEFGHIJKLMNOPQRSTUVWXYZ"
)
thresh = cv2.bitwise_not(thresh)

print("Letra detectada:", texto.strip())

cv2.imwrite("celda_procesada.png", thresh)
print("imagen guardada")

cv2.imwrite("celda_2_3.png", celda)
print("✅ Celda recortada correctamente")

cv2.imwrite("sopa_marcada.png", img)
print("✅ Celda marcada en rojo")

cv2.imwrite("sopa_cuadricula.png", img)
print("✅ Imagen guardada como sopa_cuadricula.png")

