def encode(message, rails):
    if rails < 1:
        raise ValueError("Rails must be a positive integer.")
    
    rail_list = [''] * rails
    direction = 1  # 1 for down, -1 for up
    rail_index = 0

    for char in message:
        print(f"Placing '{char}' in rail {rail_index}")  # Debug statement
        rail_list[rail_index] += char
        rail_index += direction
        print(f"Current rail index: {rail_index}, direction: {direction}")  # Debug statement

        if rail_index == rails:  # Change direction
            rail_index = rails - 2
            direction = -1
        elif rail_index < 0:  # Change direction
            rail_index = 1
            direction = 1

    return ''.join(rail_list)
        raise ValueError("Rails must be a positive integer.")
    
    rail_list = [''] * rails
    direction = 1  # 1 for down, -1 for up
    rail_index = 0

    for char in message:
        rail_list[rail_index] += char
        rail_index += direction

        if rail_index == rails:  # Change direction
            rail_index = rails - 2
            direction = -1
        elif rail_index < 0:  # Change direction
            rail_index = 1
            direction = 1

    return ''.join(rail_list)


def decode(encoded_message, rails):
    if rails < 1:
        raise ValueError("Rails must be a positive integer.")
    
    rail_length = [0] * rails
    direction = 1  # 1 for down, -1 for up
    rail_index = 0

    # First, determine the length of each rail
    for char in encoded_message:
        rail_length[rail_index] += 1
        rail_index += direction

        if rail_index == rails:  # Change direction
            rail_index = rails - 2
            direction = -1
        elif rail_index < 0:  # Change direction
            rail_index = 1
            direction = 1

    # Create the rails
    rail_list = [''] * rails
    index = 0

    # Fill the rails with the encoded message
    for i in range(rails):
        for j in range(rail_length[i]):
            rail_list[i] += encoded_message[index]
            index += 1

    # Read the message in a zig-zag pattern
    decoded_message = []
    rail_index = 0
    direction = 1

    for _ in range(len(encoded_message)):
        decoded_message.append(rail_list[rail_index][0])
        rail_list[rail_index] = rail_list[rail_index][1:]  # Remove the used character
        rail_index += direction

        if rail_index == rails:  # Change direction
            rail_index = rails - 2
            direction = -1
        elif rail_index < 0:  # Change direction
            rail_index = 1
            direction = 1

    return ''.join(decoded_message)
