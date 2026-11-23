import re

def starts_with_number(text):
    return re.match(r"\d+", text) is not None

def first_number(text):
    match = re.search(r"\d+", text)
    return int(match.group()) if match else None

def is_whole_number(text):
    return re.fullmatch(r"\d+", text) is not None


samples = ["42 apples", "apples 42", "42", "forty-two", ""]

for s in samples:
    print(
        f"{repr(s):<12} "
        f"match={str(starts_with_number(s)):<5} "
        f"search={str(first_number(s)):<5} "
        f"fullmatch={is_whole_number(s)}"
    )
    