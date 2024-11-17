def abbreviate(words):
    words = words.replace('-', ' ')
    return ''.join(word[0].upper() for word in words.split() if word)
