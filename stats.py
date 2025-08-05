def get_num_words(contents):
    words = contents.split()
    return len(words)


def get_num_chars(contents):
    lower = contents.lower()
    chars = list(lower)
    counts = dict()
    seen = set()
    duplicates = []
    char_list = []
    for char in chars:
        char_list.append(char)
    for char in char_list:
        if char in seen:
            duplicates.append(char)
        else:
            seen.add(char)
    for char in duplicates:
        if char in seen:
            counts[char] = counts.get(char, 1) + 1
    return counts
