import os
import pytesseract
import cv2 as cv
from typing import Callable

def scan_directory_for_images (directory: str, search_text: str, output_directory: str, processor: Callable):
    for subdir, _, files in os.walk(directory):

        for file in files:

            if file.lower().endswith(('.png', '.jpg', '.jpeg')):
                image_path = os.path.join(subdir, file)

                try:
                    processor(image_path, search_text, output_directory)

                except Exception as e:
                    print(f"Error processing {image_path}: {e}")
                    return ""
