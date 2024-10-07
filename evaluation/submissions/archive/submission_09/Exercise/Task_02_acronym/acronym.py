def abbreviate(words):
    import re

    # Split words by whitespace and hyphens, remove punctuation
    words = re.split(r'[-\s]+', words)
    acronym = ''.join(word[0].upper() for word in words if word)
    return acronym
    
