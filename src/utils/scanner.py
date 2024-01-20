import os
from typing import Callable
from progress.bar import Bar
from typing import List


def scan_directory_for_images(directory: str, search_text: str, output_directory: str, processor: Callable):
    image_paths = find_all_images(directory)

    bar = Bar("Loading", fill="=", suffix="%(percent)d%%", max=len(image_paths))

    for image_path in image_paths:
        try:
            processor(image_path, search_text, output_directory)
            bar.next()

        except Exception as e:
            print(f"Error processing {image_path}: {e}")
            return ""

    bar.finish()


def find_all_images(directory: str):
    image_paths: List[str] = []

    for subdir, _, files in os.walk(directory):
        for file in files:
            if file.lower().endswith((".png", ".jpg", ".jpeg")):
                image_paths.append(os.path.join(subdir, file))

    return image_paths
