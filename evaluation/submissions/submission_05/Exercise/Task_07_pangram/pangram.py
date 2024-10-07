def is_pangram(sentence):
    alphabet = set('abcdefghijklmnopqrstuvwxyz')
    return alphabet <= set(sentence.lower())

# Test cases
if __name__ == '__main__':
    test_sentences = [
        'The quick brown fox jumps over the lazy dog',
        'Hello World',
        'Pack my box with five dozen liquor jugs',
        'This sentence is not a pangram'
    ]
    
    for sentence in test_sentences:
        print(f'"{sentence}" is a pangram: {is_pangram(sentence)}')
