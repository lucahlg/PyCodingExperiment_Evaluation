def transpose(text):
    # Split the input text into lines
    lines = text.splitlines()
    
    # Determine the maximum length of the lines
    max_length = max(len(line) for line in lines)
    
    # Pad lines to the left with spaces
    padded_lines = [line.rjust(max_length) for line in lines]
    
    # Transpose the padded lines
    transposed = []
    for col in range(max_length):
        new_row = ''.join(line[col] for line in padded_lines)
        transposed.append(new_row.rstrip())  # Remove trailing spaces
    
    # Join the transposed lines into a single string
    return '\n'.join(transposed)
