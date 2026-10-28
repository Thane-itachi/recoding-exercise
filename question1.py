# problem 1: Find the Largest Number in a List

def find_largest(numbers):
    if not numbers:
        return None

    largest = numbers[0]

    for num in numbers[1:]:
        if num > largest:
            largest = num

    return largest            
# numbers = [3, 41, 56, 21, 76, 9]
# numbers = [-10, -5, -2, -18]
numbers = []
print(find_largest(numbers))