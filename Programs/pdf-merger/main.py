import PyPDF2

pdfFiles = ["sample_1.pdf", "sample_2.pdf"] # put your pdf file here to merge
merger = PyPDF2.PdfMerger()

for filename in pdfFiles:
    pdFile = open(filename, 'rb')
    pdfReader = PyPDF2.PdfReader(pdFile)
    merger.append(pdfReader)
pdFile.close()
merger.write('merged.pdf')