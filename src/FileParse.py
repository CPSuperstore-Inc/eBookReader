import os
from tkinter import messagebox

import PyPDF2
from gensim.summarization.summarizer import summarize           # pip3 install gensim

import src.GlobalVariable as GlobalVariable

if not os.path.isdir(GlobalVariable.FILE_SAVE_DIR):
    os.makedirs(GlobalVariable.FILE_SAVE_DIR)



def extract_file_text(path):
    if path.endswith(".abf") or path.endswith(".sabf"):
        return path
    pdf_file = open(path, 'rb')
    pdf_reader = PyPDF2.PdfFileReader(pdf_file)

    start = 1

    filename = os.path.split(path)[1]
    filename = filename[:filename.index(".")]
    filename = os.path.join(GlobalVariable.FILE_SAVE_DIR, filename + ".abf")

    error_pages = []

    with open(filename, 'w') as f:
        for page in range(start - 1, pdf_reader.numPages):
            try:
                text = pdf_reader.getPage(page).extractText().replace("\n", "")
                page += 1
                text = text.encode('ascii', 'ignore')
                text = str(text)[2:-1]
                f.write(text + "\n")
            except KeyError:
                error_pages.append(page)
                f.write("Error Parsing Page" + "\n")
            f.write(GlobalVariable.PAGE_DELIMITER + "\n")

    if len(error_pages) > 0:
        messagebox.showerror(
            "Page Process Error", "An Unknown Error Has Occurred While Processing The Following Pages:\n" +
                                  ", ".join(map(str, error_pages)) + "\n\n"
                                  "The Pages Have Been Skipped, And The Rest Of The Pages Will Be Used As Normal"
        )
    return filename


def read_file(path):
    with open(path, 'r') as f:
        data = f.read().replace("\n", "").split(GlobalVariable.PAGE_DELIMITER)
        data = list(filter(lambda s: s != "", data))
        return data


def generate_summary(path, ratio):
    try:
        return summarize("\n".join(read_file(path)), ratio=ratio)
    except ValueError:
        messagebox.showerror("File Too Short!", "The Input File Could Not Be Summarized As It Is Too Short!\nFiles Must Be More Than One Sentence To Properly Summarize!")
        return False