from tkinter import *
from tkinter import filedialog
from tkPDFViewer import tkPDFViewer as pdf
import os

def browseFiles():
    global v1
    filename= filedialog.askopenfilename(initialdir=os.getcwd(),title='Select file',filetypes=[("PDF files", "*.pdf")])
    if filename:
        
        v1 = pdf.ShowPdf()
        v2 = v1.pdf_view(root, pdf_location=filename, width=77, height=100)
        v2.pack(pady=(0, 0))
root=Tk()
root.geometry('630x700')
root.title('pdf')
root.configure(bg='white')


Button(root,text='open',command=browseFiles,width=40).pack()
root.mainloop()
