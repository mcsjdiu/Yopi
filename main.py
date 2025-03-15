import pyautogui
import cv2 # type: ignore
import pytesseract # type: ignore

# Path ke tesseract executable
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'

def capture_and_recognize_text():
    # Ambil tangkapan layar
    screenshot = pyautogui.screenshot()
    screenshot = cv2.cvtColor(np.array(screenshot), cv2.COLOR_RGB2BGR)

    # Gunakan tesseract untuk mengenali teks
    text = pytesseract.image_to_string(screenshot)

    # Tampilkan teks yang dikenali
    print("Teks yang dikenali: ", text)

if __name__ == "__main__":
    capture_and_recognize_text()