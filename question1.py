# problem 1: Find the Largest Number in a List

def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers:
        if num > largest:
            largest = num

    return largest            
# numbers = [3, 41, 56, 21, 76, 9]
numbers = [-10, -100, -45, -150]
# numbers = []
print(find_largest(numbers))