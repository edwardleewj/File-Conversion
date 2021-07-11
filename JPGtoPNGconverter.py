import os
import sys
from pathlib import Path
from tkinter import Tk
from tkinter.filedialog import askdirectory
from tkinter.messagebox import showinfo
from PIL import Image


def jpg_to_png(jpg, png):
    counter = 0
    for img in os.listdir(f'{jpg}'):
        if img.endswith('.jpg'):
            name = Path(f'{img}').stem
            img_obj = Image.open(f'{jpg}\\{img}')
            img_obj.save(f'{png}\\{name}.png', 'png')
        counter += 1
    showinfo(title='Conversion Complete', message=f'{counter} images were converted.')


try:
    input_folder = sys.argv[1]
    output_folder = sys.argv[2]
except IndexError:
    Tk().withdraw()
    cwd = os.getcwd()
    input_folder = askdirectory(title='Select the directory containing the jpg images to be converted', initialdir=cwd)
    output_folder = askdirectory(title='Select or Create directory for the converted images to be saved',
                                 initialdir=cwd)

try:
    os.mkdir(f'{output_folder}')
except FileExistsError:
    pass

jpg_to_png(input_folder, output_folder)
