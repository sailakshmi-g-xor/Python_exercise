import re

def extract_numbers(text):
    return re.findall(r"-?\d+(?:\.\d+)?", text)

def extract_hashtags(text):
    return re.findall(r"#\w+", text)

def extract_pairs(text):
    return re.findall(r"(\w+)=(\w+)", text)


text = (
    "Order 1042 shipped on 14 March: 3 items, total 59.97 EUR, "
    "discount -5.5 applied. Tags: #sale #newArrival #eco_friendly"
)

settings = "mode=fast; retries=3; name=Zed; level=7"

numbers = extract_numbers(text)
total = round(sum(float(n) for n in numbers), 2)

hashtags = extract_hashtags(text)
pairs = extract_pairs(settings)

print("numbers:", numbers)
print("sum:", total)
print("hashtags:", hashtags)
print("pairs:", pairs)
print("as dict:", dict(pairs))