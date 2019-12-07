import tkinter as tk
import tkinter.filedialog
from tkinter import *
import os
import sys
from tkinter import messagebox

import src.GlobalVariable as GlobalVariable


def home_page():
    def browse_file():
        file_path.set(tkinter.filedialog.askopenfilename(title="Select eBook File", filetypes = (("PDF files","*.pdf"),)))

    def set_file():
        if not os.path.isfile(file_path.get()):
            messagebox.showwarning("No File Selected!", "Please Select A File Before Clicking On The \"Open\" Button!")
            return
        GlobalVariable.FILE_PATH = file_path.get()
        root.destroy()

    def open_recent():
        try:
            filename = file_list[recent_files.curselection()[0]]
        except IndexError:
            messagebox.showwarning("No File Selected!", "Please Select A File Before Clicking On The \"Open\" Button!")
            return
        if filename.endswith(".abf"):
            GlobalVariable.FILE_PATH = os.path.join(GlobalVariable.BOOKS_DIR, filename)
            root.destroy()

    file_list = os.listdir(GlobalVariable.BOOKS_DIR)

    root = tk.Tk()

    root.title(GlobalVariable.APP_NAME)
    root.iconbitmap(GlobalVariable.ICON_PATH)
    root.protocol("WM_DELETE_WINDOW", sys.exit)

    file_path = StringVar(root)

    tk.Label(root, text=GlobalVariable.APP_NAME).grid(row=1, column=1, columnspan=3, sticky=N+S+E+W)

    tk.Label(root, text="Open File:").grid(row=2, column=1, sticky=W)
    tk.Entry(root, textvariable=file_path, width=50).grid(row=3, column=1, sticky=N+S+E+W)
    tk.Button(root, text="  Browse...  ", command=browse_file).grid(row=3, column=2, sticky=N+S+E+W)
    tk.Button(root, text="  Open File  ", command=set_file).grid(row=4, column=2, sticky=N+S+E+W)

    tk.Label(root, text="Recent Files:").grid(row=5, column=1, sticky=W)

    recent_files = Listbox(root)
    recent_files.grid(row=6, column=1, columnspan=3, sticky=N+S+E+W)

    for item in file_list:
        recent_files.insert(END, item)

    tk.Button(root, text="Open Selected Recent File", command=open_recent).grid(row=7, column=1, columnspan=2, sticky=N+S+E+W)

    root.mainloop()