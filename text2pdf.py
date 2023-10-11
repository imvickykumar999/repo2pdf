
import os
from urllib.parse import urlparse

from fpdf import FPDF
from PyPDF2 import PdfMerger, PdfReader

def convert(pdf_path = 'myfile.txt'):
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open(pdf_path, "r", encoding="unicode_escape")

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1)

    final = f'{pdf_path.split(".")[0]}.pdf'
    pdf.output(final)
    return final

def clone_repo(repo):
    try:
        os.system(f'git clone {repo}')
    except Exception as e:
        print(e)

repo = 'https://github.com/imvickykumar999/sqlzoo-solutions'
clone_repo(repo)

merger = PdfMerger()
a = urlparse(repo)
folder = os.path.basename(a.path)

exclude = set(['.git'])
for root, dirs, files in os.walk(folder, topdown=True):
    dirs[:] = [d for d in dirs if d not in exclude]

    for name in files:
        file = os.path.join(root, name)
        merger.append(PdfReader(open(convert(file), 'rb')))

merger.write("merged.pdf")
