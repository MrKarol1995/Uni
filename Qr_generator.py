import qrcode
import cv2

def generate_qr_code(text, file_name):
    """
    Generuje kod QR z podanym tekstem i zapisuje go do pliku.

    """
    qr = qrcode.QRCode(
        version=1,
        error_correction=qrcode.constants.ERROR_CORRECT_L,
        box_size=10,
        border=4
    )
    qr.add_data(text)
    qr.make(fit=True)

    img = qr.make_image(fill_color="black", back_color="white")
    img.save(file_name)
    print(f'Kod QR został zapisany do pliku: {file_name}')

def read_qr_code(file_name):
    """
    Odczytuje zawartość kodu QR z obrazka.

    """
    image = cv2.imread(file_name)
    gray = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

    detector = cv2.QRCodeDetector()
    data, bbox, _ = detector.detectAndDecode(gray)

    if bbox is not None:
        print(f'Odczytana zawartość kodu QR: {data}')
        return data
    else:
        print('Nie udało się odczytać kodu QR.')
        return None


text = "nigas in paris"
qr_file_name = "ale3k.jpg"
qqr = "kod2.jpg"

# Generowanie kodu QR
generate_qr_code(text, qr_file_name)

read_qr_code(qqr)


