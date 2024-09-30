def find_anagrams(word, candidates):
    # Normalize the target word by sorting its letters
    sorted_word = sorted(word.lower())
    
    # Find anagrams by comparing sorted letters
    return [candidate for candidate in candidates if candidate.lower() != word.lower() and sorted(candidate.lower()) == sorted_word]
