import itertools

def solve(puzzle):
    words = puzzle.replace('+', ' ').replace('=', ' ').split()
    unique_letters = set(''.join(words))
    
    if len(unique_letters) > 10:
        raise ValueError("Too many unique letters in the puzzle.")
    
    for digits in itertools.permutations(range(10), len(unique_letters)):
        letter_to_digit = dict(zip(unique_letters, digits))
        
        # Check for leading zeros
        if any(letter_to_digit[word[0]] == 0 for word in words if len(word) > 1):
            continue
        
        # Evaluate the equation
        left_side = sum(int(''.join(str(letter_to_digit[letter]) for letter in word)) for word in words[:-1])
        right_side = int(''.join(str(letter_to_digit[letter]) for letter in words[-1]))
        
        if left_side == right_side:
            return letter_to_digit
    return None

# Test case
if __name__ == '__main__':
    puzzle = 'SEND + MORE = MONEY'
    solution = solve(puzzle)
    print(f'Solution for puzzle "{puzzle}": {solution}')
