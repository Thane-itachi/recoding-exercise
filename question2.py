# Problem 2: Find the Smallest Number in a List

def find_smallest(numbers):
    if not numbers:
        return None

    smallest = numbers[0]

    for num in numbers:
        if num < smallest:
            smallest = num

    return smallest           
# numbers = [8, 3, 12, 1, 7]
# numbers = [-3, -10, -1, -6]
numbers = []
print(find_smallest(numbers))