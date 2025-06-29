def count_book_words(path_file):
    with open(path_file) as f:
        b = f.read()
    return len(b.split())

def count_book_chars_dict(path_file):
    d = {}

    with open(path_file) as f:
        b = f.read()
        b = b.lower()
    
    for c in b:
        if c in d:
            # print("character is in dictionary")
            x = d[c] + 1
            d[c] = x
        else:
            # print("adding character to dictionary")
            d[c] = 1

    return d

def count_book_chars_list(path_file):
    l = []

    j = count_book_chars_dict(path_file)

    for char, count in j.items():
        l.append({"name":char, "num":count})

    return l
