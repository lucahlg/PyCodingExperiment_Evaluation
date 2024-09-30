import re
from collections import Counter

def count_words(sentence):
    sentence = sentence.lower()

    words = re.findall(r"\b[\w']+\b", sentence)

    word_count = Counter(words)
    
    return word_count

# Example
example = "That's the password: 'PASSWORD 123'!, cried the Special Agent.\nSo I fled."
result = count_words(example)

for word, count in result.items():
    print(f"{word}: {count}")
