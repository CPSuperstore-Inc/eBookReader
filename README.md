# eBookReader
A Small Application For Reading eBooks Using Speech Synthesis.

## Dependencies
This project relies on the `pyttsx3` library. To install, please run the command:

`pip3 install pyttsx3` or `pip install pyttsx3` depending on how your Python environment is set up.

If I have missed anything, please submit an issue to let me know at (https://github.com/CPSuperstore-Inc/eBookReader/issues)

## Usage
To use this application, simply run `eBookReader.py`. This **MUST** be run with a Python3 interpreter.

Note that it may take a bit for the UI to actually launch.

Note that currently, only .pdf files are supported, but more will be coming soon.

This will open the main UI. You are given 2 options here as to how you would like to open your eBook.

_Option 1_: Click the "Browse..." button at the top of the UI to locate a .pdf file on your computer

_Option 2_: Once a file has been open, it will be listed under the "Recent Files" section, with the file extension .abf.
You may select any file here, and click "Open Selected Recent File".

Once the file is open, you can manipulate the file. There are 6 buttons on the bottom of the page. Described from left to right:

_Previous Page_: Navigates you to the previous page of the eBook

_Next Page_: Navigates you to the next page of the eBook

_Read This Page_: Reads the current page to you with a synthesized voice

_Read All Pages_: Reads the current page, and all pages after, to you with a synthesized voice

_Stop Reading_: Stops the synthesized voice if it is reading

_Home_: Returns you to the home page where you selected the file

More features coming soon. If you have any issues, feel free to open an issue on GitHub at (https://github.com/CPSuperstore-Inc/eBookReader/issues)
 
Enjoy :)