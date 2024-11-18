def accumulate(collection, operation):
    result = []
    for item in collection:
        result.append(operation(item))
    return result
    
def square(x): 
    return x * x

numbers = [1, 2, 3, 4, 5]
squared_numbers = accumulate(numbers, square) 
print(squared_numbers)