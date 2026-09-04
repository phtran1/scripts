import pypdf
import sys

inputs = sys.argv[1:]

def pdf_merge(pdf_list):
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        merger.append(pdf)
    merger.write("merged.pdf")
    print("PDF files merged into merged.pdf.")

def water_mark(pdf_list, watermark):
    wtr = pypdf.PdfReader(watermark)
    merger = pypdf.PdfWriter()
    for pdf in pdf_list:
        reader = pypdf.PdfReader(pdf)
        for p in reader.pages:
            p.merge_page(wtr.pages[0])
            merger.add_page(p)
    merger.write("marked.pdf")
    print("Watermark added to the PDF files.")

# pdf_merge(inputs)
water_mark(inputs, "wtr.pdf")