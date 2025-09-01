def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    lower = text.lower()
    chars = {}
    for char in lower:
        chars[char] = chars.get(char, 0) + 1
    return chars

def sort_on(items):
    return items["num"]

def sort_chars(num_chars):
    list_of_dicts = [
        {"char": char, "num": count} 
        for char, count in num_chars.items()
        if char.isalpha()
    ]
    list_of_dicts.sort(reverse=True, key=sort_on)
    return list_of_dicts
