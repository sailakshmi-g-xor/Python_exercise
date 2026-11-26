import sys
def is_palindrome(text):
    cleaned = " ".join(
                    ch.lower() 
                    for ch in text 
                    if ch.isalnum())
    return cleaned == cleaned[::-1]
    
for line in sys.stdin:
    line = line.rstrip("\r\n")

    if not line.strip():    
        continue

    if is_palindrome(line):
        print(f"{line!r} -> yes")
    else:
        print(f"{line!r} -> no")

