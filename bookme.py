
# pip install gitpython fpdf

import os
from git import Repo
from urllib.parse import urlparse

from fpdf import FPDF
from PyPDF2 import PdfMerger, PdfReader

try: os.mkdir('output')
except: pass

try: os.mkdir('input')
except: pass

def convert(pdf_path = 'myfile.txt'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 10)
    f = open(pdf_path, "r", encoding="unicode_escape")

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1)

    final = f'{pdf_path.split(".")[0]}.pdf'
    pdf.output(final)
    return final

def clone_repo(repo, folder):
    os_folder = os.path.join('input', folder)
    try: Repo.clone_from(repo, os_folder)
    except Exception as e: print(e)

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
        try:
            pdf = open(convert(file), 'rb')
            merger.append(PdfReader(pdf))
        except:
            pass

output = f"output/{folder}.pdf"
merger.write(output)
