from itertools import islice


with open("data/notes.txt", "r", encoding="utf-8") as file:
    i = 1
    for line in islice(file,5):
        clean_line = line.rstrip("\r\n")
        print(f"{i}:{clean_line:>{3}}")
        i = i+1
def file_stats(path):
    with open(path,"r",encoding="utf-8") as file:
        lines = file.readlines()
        print(f"Lines:{len(lines)}")
        print(f"Words:{sum(len(line.split()) for line in lines)}")
        print(f"Characters:{sum(len(line) for line in lines)}")
        print(f"Blank lines:{sum(1 for line in lines if not line.strip())}")

path = "data/notes.txt"
file_stats(path)