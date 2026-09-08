def chunk_text(text, size, overlap):
    chunks = []
    start = 0
    while start < len(text):
        end = start + size
        chunks.append(text[start:end])
        start += size - overlap
    return chunks

text = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"

result = chunk_text(text, 10, 3)

print(result)
