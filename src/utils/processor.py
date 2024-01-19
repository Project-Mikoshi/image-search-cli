import os
import pytesseract
import cv2 as cv
from pathlib import Path

def search_text_in_image_text (image_path: str, search_text: str, output_directory: str):
    image = cv.imread(image_path)

    image_data = pytesseract.image_to_data(
        image=image,
        output_type=pytesseract.Output.DICT
    )

    image_text_data = image_data['text']

    for i in range(len(image_text_data)):
        text: str = image_text_data[i]

        if search_text.lower() in text.lower():
            coordinates = (image_data['left'][i], image_data['top'][i], image_data['width'][i], image_data['height'][i])

            hightlighted_image = _hightlight_image(image, coordinates)

            _output_result(hightlighted_image, image_path, output_directory)

def _hightlight_image (image: cv.Mat, coordinates: tuple):
    (x, y, w, h) = coordinates
    hightlight_color = (0, 0, 255)
    padding = 10

    return cv.rectangle(image, (x - padding, y - padding), (x + w + padding, y + h + padding), hightlight_color, 2)

def _output_result (image: cv.Mat, image_path: str, output_directory: str):
    if (not os.path.exists(output_directory)):
        os.makedirs(output_directory)

    image_name = os.path.basename(image_path)
    output_path = os.path.join(output_directory, image_name)

    cv.imwrite(output_path, image)

    with open(os.path.join(output_directory, f"{Path(image_path).stem}-path.txt"), "w") as result_file:
        result_file.write(image_path)
