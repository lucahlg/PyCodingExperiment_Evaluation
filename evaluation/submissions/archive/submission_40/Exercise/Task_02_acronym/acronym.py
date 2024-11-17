def abbreviate(words):
    import re
    words = re.sub(r'[-]', ' ', words)
    words = re.sub(r'[^\w\s]', '', words)
    return ''.join(word[0].upper() for word in words.split())
