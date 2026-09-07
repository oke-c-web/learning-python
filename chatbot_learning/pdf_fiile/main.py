from  pypdf import PdfReader

reader =  PdfReader("myFile.pdf")
print(len(reader.pages))

full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

pde_fille = full_text[:200]
print(pde_fille)
    