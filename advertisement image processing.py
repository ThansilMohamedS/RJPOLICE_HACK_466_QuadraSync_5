import pytesseract
from PIL import Image
from googlesearch import search
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR' 
def ocr(image_path):
    try:
        image = Image.open(image_path)
        text = pytesseract.image_to_string(image)
        return text.strip()
    except Exception as e:
        print(f"Error in OCR function: {e}")
        return None

def search_text(text):
    try:
        search_results = list(search(text, num=4, stop=4))
        return search_results
    except Exception as e:
        print(f"Error in search_text function: {e}")
        return None

def is_text_present_in_search(image_path):
    extracted_text = ocr(image_path)
    if extracted_text is None:
        return False

    search_results = search_text(extracted_text)
    if search_results is None:
        return False

    if any(extracted_text.lower() in result.lower() for result in search_results):
        return True
    else:
        return False

image_path = r'C:\Users\Thansil\Desktop\Python\dominoz.png'
if is_text_present_in_search(image_path):
    print("The image is true.")
else:
    print("The image is not true.")