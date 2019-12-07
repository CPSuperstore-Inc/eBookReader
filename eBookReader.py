import src.GlobalVariable as GlobalVariable
from src.BookReader import read_book
from src.FileParse import extract_file_text, read_file
from src.Home import home_page

while True:
    home_page()
    extracted = extract_file_text(GlobalVariable.FILE_PATH)
    read_book(extracted, read_file(extracted))
