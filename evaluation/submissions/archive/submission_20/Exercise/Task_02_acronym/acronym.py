def abbreviate(words):
    import re

    
    

    words = re.sub(r'[-]', ' ', words)
    words = re.sub(r'[^a-zA-Z0-9 ]', '', words)
    return ''.join(word[0].upper() for word in words.split())
    words = re.sub(r'[^a-zA-Z0-9 ]', '', words)
    return ''.join(word[0].upper() for word in words.split())
    words = re.sub(r'[^a-zA-Z0-9 ]', '', words)
    return ''.join(word[0].upper() for word in words.split())
    words = re.sub(r'[^a-zA-Z0-9 ]', '', words)
    return ''.join(word[0].upper() for word in words.split())
