from openai import OpenAI 
from dotenv import load_dotenv

load_dotenv()

client = OpenAI()

text = "John chose engineering."

response = client.embeddings.create(
    model="text-embedding-3-small",
    input = text
)

vector = response.data[0].embedding 
print(vector)