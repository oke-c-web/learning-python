color = {"red","blue","green","yellow"}
print(color)

color.add("black")
print(color)

print("blue" in color)
print("white" in color) 


def word_count(text):
    return len(text.split())

try:
    with open("myfile.txt","r") as val:
        contents = val.read()
        print(contents)
except FileNotFoundError:
    print("File not found")

print(word_count("i an leaning python today"))