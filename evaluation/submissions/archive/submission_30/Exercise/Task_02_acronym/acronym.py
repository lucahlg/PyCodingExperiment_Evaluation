def abbreviate(words):
    import re
    return ''.join(word[0].upper() for word in re.split(r'[-\s]+', words) if word:
