import os
import sys
import threading
import tkinter as tk
from tkinter import *
from tkinter.scrolledtext import ScrolledText

import pyttsx3  # pip3 install pyttsx3

import src.GlobalVariable as GlobalVariable

engine = pyttsx3.init()

engine.say("    ")
mngr = threading.Thread(target=engine.startLoop)
mngr.setDaemon(True)
mngr.start()
engine.stop()

stopped = False

def read_book(name, data, page=1):
    def change_page(delta):
        nonlocal page
        nonlocal text

        page += delta
        if page <= 0:
            page -= delta
            return

        if page > pages:
            page -= delta
            return

        page_progress.set("Page {}/{}".format(page, pages))

        text = data[page - 1]
        page_text.configure(state=NORMAL)
        page_text.delete(1.0, END)
        page_text.insert(INSERT, text)
        page_text.configure(state=DISABLED)

    def read_page():
        engine.say("Page {}.".format(page))
        engine.say(text)
        try:
            engine.startLoop()
        except RuntimeError:
            pass


    def continuous_read():
        global stopped

        for i in range(page, pages + 1):
            read_page()
            while engine.isBusy():
                pass
            if stopped:
                break
            change_page(1)
        stopped = False


    def spawn_thread(target):
        t = threading.Thread(target=target)
        t.setDaemon(True)
        t.start()

    def stop():
        global stopped
        stopped = True
        engine.stop()

    pages = len(data)
    text = ""

    name = os.path.split(name)[1]
    name = name[:name.index(".")]

    root = tk.Tk()

    root.title(GlobalVariable.APP_NAME)
    root.iconbitmap(GlobalVariable.ICON_PATH)
    root.protocol("WM_DELETE_WINDOW", sys.exit)

    root.grid_columnconfigure(4, uniform="foo")

    page_progress = StringVar(root, "Page {}/{}".format(page, pages))

    tk.Label(root, text=name).grid(row=1, column=1, columnspan=5)
    tk.Label(root, textvariable=page_progress).grid(row=2, column=1, columnspan=5)
    page_text = ScrolledText(root)
    page_text.grid(row=3, column=1, columnspan=5)

    tk.Button(root, text="Previous Page", command=lambda: change_page(-1)).grid(row=4, column=1, sticky=N+S+E+W)
    tk.Button(root, text="Next Page", command=lambda: change_page(1)).grid(row=4, column=2, sticky=N+S+E+W)
    tk.Button(root, text="Read This Page", command=lambda: spawn_thread(read_page)).grid(row=4, column=3, sticky=N+S+E+W)
    tk.Button(root, text="Read All Pages", command=lambda: spawn_thread(continuous_read)).grid(row=4, column=4, sticky=N+S+E+W)
    tk.Button(root, text="Stop Reading", command=stop).grid(row=4, column=5, sticky=N+S+E+W)

    tk.Button(root, text="Home", command=root.destroy).grid(row=5, column=1, sticky=N+S+E+W)

    change_page(0)

    root.mainloop()