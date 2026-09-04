def count_words_in_file(path):
    try:
        with open(path, "r") as fpy:
            contents = fpy.read()
            return len(contents.split())
    except FileNotFoundError:
        return 0


with open("test.txt", "w") as f:
    f.write("the quick brown fox jumps")

print(count_words_in_file("test.txt"))     
print(count_words_in_file("missing.txt")) 