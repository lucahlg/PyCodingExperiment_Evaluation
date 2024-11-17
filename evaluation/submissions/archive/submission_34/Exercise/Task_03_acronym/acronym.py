def abbreviate(words):
    import re
    words = re.sub(r'[-]', ' ', words)
    return ''.join(word[0].upper() for word in words.split() if word)}
