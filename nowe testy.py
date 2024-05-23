from PIL import Image
import sys


# ścieżka do pliku grafiki, która będzie użyta jako znak wodny
watermark_path = "watermark.jpg"

# pobierz ścieżkę do pliku grafiki od użytkownika
image_path = sys.argv[1]

# załaduj obrazki
image = Image.open(image_path)
watermark = Image.open(watermark_path)

# ustaw przezroczystość znaku wodnego (opcjonalne)
watermark.putalpha(128)

# oblicz pozycję znaku wodnego na obrazku
position = (image.size[0] - watermark.size[0], image.size[1] - watermark.size[1])

# dodaj znak wodny do obrazka
image.paste(watermark, position, watermark)

# zapisz zmodyfikowany obrazek
image.save("watermarked_image.jpg")
