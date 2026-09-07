from pypdf import PdfReader

reader = PdfReader("myfile.pdf")
print(len(reader.pages))

first_page = reader.pages[0]
text = first_page.extract_text()
print(text)

val_page = ""
for page in reader.pages:
    val_page += page.extract_text() + "\n"
    print(val_page)
