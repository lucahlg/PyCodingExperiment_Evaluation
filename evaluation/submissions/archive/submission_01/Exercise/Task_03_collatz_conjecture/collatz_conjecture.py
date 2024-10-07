def steps(n):
    if n <= 0:
        raise ValueError("Input must be a positive integer.")
    
    collatz_steps = 0

    while n != 1:
        if n % 2 == 0:  
            n = n // 2
        else:           
            n = 3 * n + 1
        collatz_steps += 1

    return collatz_steps
