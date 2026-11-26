def even_squares(nums):
    squares = [n*n for n in range(1,nums+1) if(n%2==0)]
    return squares
def word_lengths(words):
    d = [{w : len(w)} for w in words]
    return d
def first_letters(words):
    letters = [w[0] for w in words]
    return letters
def flatten(matrix):
    flat = [i for l in matrix for i in l]
    return flat
def transpose(matrix):
    trans = [[matrix[i][j] for i in range(len(matrix))] for j in range(len(matrix[0]))]
    print(trans)
print(even_squares(10))
print(word_lengths(["apple", "kiwi", "banana", "fig"]))
print(first_letters(["apple", "avocado", "banana", "blueberry", "cherry"]))
print(flatten([[1, 2, 3], [4, 5, 6]]))
transpose([[1, 2, 3], [4, 5, 6]])
