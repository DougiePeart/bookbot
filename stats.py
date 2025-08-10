def get_num_words(text):
    words = text.split()
    return len(words)


def get_num_chars(text):
    lower = text.lower()
    chars = {}
    for char in lower:
        chars[char] = chars.get(char, 0) + 1

def get_chars_dict(text):
    chars = {}
    for c in text:
        lowered = c.lower()
        if lowered in chars:
            chars[lowered] += 1
        else:
            chars[lowered] = 1
    return chars
