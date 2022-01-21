# https://pyfpdf.readthedocs.io/en/latest/reference/FPDF/index.html
# https://stackhowto.com/how-to-extract-a-zip-file-in-python/

from PIL import Image
from zipfile import ZipFile
from colorama import init, Fore, Style
import os, random
from fpdf import FPDF

init()

def b(text:str):
    return Fore.BLUE + text + Style.RESET_ALL
def y(text:str):
    return Fore.YELLOW + text + Style.RESET_ALL
def r(text:str):
    return Fore.RED + text + Style.RESET_ALL
def rand(num:int):
    return random.randint(1, 100)

file = 'in.cbz'
print( b("INFO - ") + f"Imported '{file}'" )

with ZipFile(file, 'r') as zip:
    if 'out' not in os.listdir('./'):
        print(y("WARN - ") + "'./out/' directory does not exist. Creating ...")
        os.makedirs('./out/')
        print(y("WARN - ") + "'./out/' directory created, continuing.")

    for file in os.listdir('./out/'):
        os.remove('./out/' + file)
        print( b("INFO - ") + f"Removed './out/" + file + "',")
    print(y("WARN - ") + "'./out/' directory cleared, continuing.")

    print( b("INFO - ") + f"Extracting '{file}'" )
    zip.extractall(path='./out/')
    print( b("INFO - ") + f"Extracted '{file}' to './out/'" )

if 'out.pdf' in os.listdir('./'):
    print(y("WARN - ") + "'out.pdf' already exists. Deleting ...")
    os.remove('out.pdf')
    print(y("WARN - ") + "'out.pdf' deleted, continuing.")

print( b("INFO - ") + f"Setting PDF parameters ..." )

sizer = Image.open("./out/" + os.listdir("./out/")[0])

w,h = sizer.size
w = w / 72
h = h / 72

pdf = FPDF("P", "in", (w,h))
pdf.set_auto_page_break(0)

img_list = [x for x in os.listdir('./out/')]

print( b("INFO - ") + f"Adding images to PDF" )

for img in img_list:
    pdf.add_page()
    pdf.image('./out/' + img)

print( b("INFO - ") + f"Saving to 'out.pdf'" ) # warning, depending on the size of the cbz, it may take a while to create, so do be aware
print( y("WARN - ") + f"Depending on the size of your 'cbz', this may take a while." )

pdf.output("out.pdf")

print( b("INFO - ") + f"PDF has finished creating! Enjoy!")