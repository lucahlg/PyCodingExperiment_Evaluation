def abbreviate(words):
    import re

    # Replace hyphens with spaces and remove other punctuation
    words = re.sub(r'[-]', ' ', words)
    words = re.sub(r'[^\w\s]', '', words)

    # Split the words and create the acronym
    acronym = ''.join(word[0].upper() for word in words.split())
    return acronym
    
