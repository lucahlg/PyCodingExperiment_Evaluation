def slices(series, length):
    if length < 1 or length > len(series):
        raise ValueError("Invalid length")
    
    return [series[i:i + length] for i in range(len(series) - length + 1)]

# Test the slices function
if __name__ == "__main__":
    print(slices("49142", 3))  # Expected: ['491', '914', '142']
    print(slices("49142", 4))  # Expected: ['4914', '9142']
