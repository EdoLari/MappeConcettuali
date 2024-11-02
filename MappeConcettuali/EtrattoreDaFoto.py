from PIL import Image # type: ignore
import pytesseract # type: ignore
import pytesseract

# Specifica il percorso dell'eseguibile di Tesseract
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

# Specifica il percorso di Tesseract (necessario su alcuni sistemi)
# pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe' 

# Carica l'immagine
image = Image.open('foto.jpg')

# Estrai il testo dall'immagine
testo_estratto = pytesseract.image_to_string(image)

print("Testo estratto:")
print(testo_estratto)
