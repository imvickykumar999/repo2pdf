# pip install fpdf

def pdf_border(pdf_path = 'encrypt.pdf'):
    import io
    from reportlab.pdf import PdfWriter
    writer = PdfWriter(io.BytesIO())
    page = writer.getPage()

    rectangle = page.drawRectangle(10, 10, 100, 100)
    rectangle.setStrokeColor(0, 0, 0)
    final = f'{pdf_path.split(".")[0]}.pdf'
    writer.save(final)
    return final

def convert(pdf_path = 'myfile.txt'):
    from fpdf import FPDF
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size = 15)
    f = open(pdf_path, "r")

    for x in f:
        pdf.cell(200, 10, txt = x, ln = 1)

    final = f'{pdf_path.split(".")[0]}.pdf'
    pdf.output(final)
    return final

# convert('encrypt.py')
# pdf_border('encrypt.pdf')

from PyPDF2 import PdfMerger, PdfReader
merger = PdfMerger()

merger.append(PdfReader(open(convert('encrypt.py'), 'rb')))
merger.append(PdfReader(open(convert('README.md'), 'rb')))
merger.write("merged.pdf")
