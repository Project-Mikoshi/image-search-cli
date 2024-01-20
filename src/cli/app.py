import typer
import art
from rich import print as rprint
import sys
from src.utils.processor import search_text_in_image_text
from src.utils.scanner import scan_directory_for_images
from src.utils.tesseract import is_tesseract_installed

app = typer.Typer(rich_markup_mode="rich")


@app.command("interactive")
def interactive_scan():
    search_text = typer.prompt("What's the search text?")
    search_directory = typer.prompt("What's the root directory to begin the recursive search from?")
    output_directory = typer.prompt("What's the output directory to display the highlighted images and their path?")

    if not search_text or not search_directory or not output_directory:
        typer.Abort()

    rprint("Searching")
    scan_directory_for_images(search_directory, search_text, output_directory, search_text_in_image_text)


@app.command("scan")
def scan(search_text: str, search_directory: str = ".", output_directory: str = "./out"):
    scan_directory_for_images(search_directory, search_text, output_directory, search_text_in_image_text)


def run():
    rprint(art.text2art("InkSpotter CLI"))

    if not is_tesseract_installed():
        rprint("Tesseract is not installed or not found in PATH. Please install it and try again.")
        sys.exit(1)

    app()
