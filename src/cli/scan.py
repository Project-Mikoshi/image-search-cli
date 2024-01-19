import argparse
from src.utils.processor import search_text_in_image_text
from src.utils.scanner import scan_directory_for_images

def run ():
  parser = argparse.ArgumentParser(description="Scan images for specific text using Tesseract OCR and openCV.")
  parser.add_argument("-t", "--text", help="Text to search for in images", required=True)
  parser.add_argument("-d", "--directory", help="Directory to scan for images")
  parser.add_argument("-o", "--output_directory", help="Directory for result output")

  args = parser.parse_args()

  search_directory: str = args.directory or "."
  output_directory: str = args.output_directory or "./out"
  search_text: str = args.text

  scan_directory_for_images(search_directory, search_text, output_directory, search_text_in_image_text)
