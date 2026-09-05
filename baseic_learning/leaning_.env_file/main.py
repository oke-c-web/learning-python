import os
from dotenv import load_dotenv

load_dotenv()

name = os.getenv("MY_NAME","Guest")

print(f"Hello, {name}!")