def count_words(sentence):
    import re
    from collections import Counter

    # Use regular expression to find words, considering contractions
    words = re.findall(r"\b[\w']+\b", sentence.lower())
    return Counter(words)
