
# pip install gitpython fpdf img2pdf

import os
from git import Repo
from urllib.parse import urlparse

import img2pdf
from fpdf import FPDF
from PyPDF2 import (
    PdfMerger, 
    PdfReader, 
    PdfWriter
)

try: os.mkdir('output')
except: pass

try: os.mkdir('input')
except: pass

pdf = FPDF()
pdf.add_page()
pdf.set_font("Arial", size = 12)

def convert(pdf_path = 'myfile.txt'):
    f = open(pdf_path, "r", encoding="unicode_escape")
    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1)

    final = f'{pdf_path.split(".")[0]}.pdf'
    pdf.output(final)
    return final


def clone_repo(repo, folder):
    os_folder = os.path.join('input', folder)

    try: 
        Repo.clone_from(repo, os_folder)
    except Exception as e: 
        print(e)


repo = input('\nEnter repo link : ')
if repo == '':
    repo = 'https://github.com/imvickykumar999/sqlzoo-solutions'

merger = PdfMerger()
a = urlparse(repo)
folder = os.path.basename(a.path)

clone_repo(repo, folder)
os_folder = os.path.join('input', folder)


exclude = set(['.git'])
for root, dirs, files in os.walk(os_folder, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]

    for name in files:
        file = os.path.join(root, name)
        ext = os.path.basename(file)
        # print('\n======>', file)

        try:
            if ext.split(".")[1].lower() in ['png', 'jpg', 'jpeg']:
                with open(file + '.pdf', "wb") as f:
                    f.write(img2pdf.convert([file]))
                file += '.pdf'

            if ext.split(".")[1].lower() != 'pdf':
                file = convert(file)

            print('======>', file)
            pdf = open(file, 'rb')
            merger.append(PdfReader(pdf))
        except:
            pass

try: 
    os.mkdir(f"output/{folder}")
except: 
    pass


output = f"output/{folder}/{folder}.pdf"
merger.write(output)

reader = PdfReader(output)
writer = PdfWriter()
writer.append_pages_from_reader(reader)


password = input('\nEnter password to encrypt : ')
if password == '':
    password = 'password'

writer.encrypt(password)
output = f"output/{folder}/{folder}_{password}.pdf"

with open(output, "wb") as out_file:
    writer.write(out_file)
