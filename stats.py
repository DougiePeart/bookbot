def get_num_words(contents):
    words = contents.split()
    return len(words)


def get_num_chars(contents):
    words = list(contents)
    chars = list(words)
    return chars.count()
