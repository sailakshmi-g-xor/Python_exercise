
def write_squares(path):
    with open(path, "w", encoding="utf-8") as file:
        file.write(f"Lines written to {path} : {n}\n")
        for i in range(1,n+1):
            file.write(f"{i} squared is {i**2}\n")
def read_squares(path):
    with open(path, "r", encoding = "utf-8") as file:
        for line in file:
            print(f"{line}")
path = "data/squares.txt"
n = int(input("Enter the number of squares to write: "))
write_squares(path)
read_squares(path)
