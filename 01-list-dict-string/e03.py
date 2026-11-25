def mask_number(number):
    return "*" * (len(number) - 4) + number[-4:]
    #return number[-4:].rjust(len(number), "*")
def reverse_word(sentence):
    return " ".join(reversed(sentence.split()))
def middle(word):
    length = len(word)
    if length % 2 == 0:
        return word[length//2 - 1:length//2+1]
    else:
        return word[length//2]
def every_other(text):
    t = text[::2]
    return t

number = "41111111111111"
sentence = "learning python is fun"
print(mask_number(number))
print(reverse_word(sentence))
print(middle("python"))
print(middle("slicing"))
print(every_other("abcdefghij"))