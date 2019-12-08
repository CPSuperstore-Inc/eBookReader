import tkinter as tk
import tkinter.filedialog
from tkinter import *
import os
import sys
from tkinter import messagebox

import src.GlobalVariable as GlobalVariable
import src.FileParse as FileParse


def get_summary_options(filename):
    def validate():
        if filename.get() == "":
            messagebox.showerror("Invalid Value!", "The Filename Must Not Be Empty!")
            return

        r = ratio.get()
        if r == "":
            messagebox.showerror("Invalid Value!", "The Ratio Must Not Be Empty!")
            return

        if not r.replace('.','',1).isdigit():
            messagebox.showerror("Invalid Value!", "The Ratio Must Be A Number Between 0 And 100")
            return

        if not 0. <= float(r) <=100:
            messagebox.showerror("Invalid Value!", "The Ratio Must Be A Number Between 0 And 100")
            return

        root.destroy()
        root.quit()

    root = tk.Tk()
    root.title(GlobalVariable.APP_NAME)
    root.iconbitmap(GlobalVariable.ICON_PATH)

    filename = StringVar(root, filename[:filename.index(".")])
    ratio = StringVar(root, "0.5")

    tk.Label(root, text="Summary Options").grid(row=1, column=1, sticky=W, columnspan=2)

    tk.Label(root, text="Output Name: ").grid(row=2, column=1, sticky=W)
    tk.Entry(root, textvariable=filename).grid(row=2, column=2, sticky=N + S + E + W, columnspan=2)

    tk.Label(root, text="Summary Ratio: ").grid(row=3, column=1, sticky=W)
    tk.Entry(root, textvariable=ratio).grid(row=3, column=2, sticky=N + S + E + W)
    tk.Label(root, text="%").grid(row=3, column=3, sticky=W)

    tk.Button(root, text="Start Summary", command=validate).grid(row=4, column=1, sticky=N+S+E+W, columnspan=3)

    root.mainloop()

    return filename.get() + ".sabf", float(ratio.get()) * 0.1


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
        GlobalVariable.FILE_PATH = os.path.join(GlobalVariable.FILE_SAVE_DIR, filename)
        root.destroy()


    def summarize_file():
        try:
            filename = file_list[recent_files.curselection()[0]]
        except IndexError:
            messagebox.showwarning("No File Selected!", "Please Select A File Before Clicking On The \"Summarize\" Button!")
            return
        options = get_summary_options(filename)

        path = os.path.join(GlobalVariable.FILE_SAVE_DIR, filename)

        data = FileParse.generate_summary(path, options[1])
        if data is False: return

        path = os.path.join(GlobalVariable.FILE_SAVE_DIR, options[0])

        with open(path, 'w') as f:
            f.write(data)

        GlobalVariable.FILE_PATH = path
        root.destroy()

    file_list = os.listdir(GlobalVariable.FILE_SAVE_DIR)

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
    tk.Button(root, text="Summarize Selected File", command=summarize_file).grid(row=8, column=1, columnspan=2, sticky=N+S+E+W)

    root.mainloop()