# Problem 9: Find the First Duplicate
# Description
# Write a function named first_duplicate(numbers) that returns the first number that appears more than once while moving from left to right.
# Return None if there are no duplicates.

# Hints
# Keep track of values you have already visited.
# For every new number, check whether it has already been seen.
# You can return immediately when you discover the first repeated value.


def first_duplicate(numbers):
    kofi = set()

    for num in numbers:
        if num in kofi:
            return num
        kofi.add(num)    
    return None 
# numbers = [4, 7, 2, 7, 5, 4]
# numbers = [1, 2, 3, 4]
numbers = [5, 3, 5]
print(first_duplicate(numbers))       