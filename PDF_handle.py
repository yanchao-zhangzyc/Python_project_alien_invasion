#encoding=utf-8
import PyPDF2
pdf1=open("Python编程：从入门到实践.pdf",'rb')
pdf2=open("Python编程：从入门到实践.pdf2",'rb')
pdf1Reader=PyPDF2.PdfFileReader(pdf1)
pdf2Reader=PyPDF2.PdfFileReader(pdf2)

pdfWriter=PyPDF2.PdfFileWriter()

for pageNum in range()