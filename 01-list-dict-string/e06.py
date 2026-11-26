def group_by_length(path):
    d = {}
    with open(path,'r',encoding='utf-8') as f:
        for word in f:
            word = word.strip()
            length = len(word)
            if length not in d:
                d[length] = []
            else:
                d[length].append(word)
    print(dict(sorted(d.items())))

path = "01-list-dict-string/data/words.txt"
group_by_length(path)