from  pypdf import PdfReader

reader =  PdfReader("myFile.pdf")
print(len(reader.pages))

full_text = ""
for page in reader.pages:
    full_text += page.extract_text()

pdf_fille = full_text[:200]
print(pdf_fille)

def chunk_text(text, size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return chunks

print(chunk_text(full_text, 200, 50))
print(len(chunk_text(full_text, 200, 50)))