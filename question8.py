# Problem 8: Check if a List Contains Duplicates
# Description
# Write a function named has_duplicates(numbers) that returns True if any number appears more than once and False otherwise.

# Hints
# You need a way to remember numbers you have already seen.
# Before storing the current number, check whether you have seen it before.
# A Python set can help with fast membership checks.

def has_duplicates(numbers):
    kofi = set()
    for num in numbers:
        if num in kofi:
            return True
        kofi.add(num)
    return False 

# numbers = [1, 2, 3, 2]
# numbers = [1, 2, 3, 4]
numbers = [1 , 6, 7, 9, 6, 9]
# numbers = []
print(has_duplicates(numbers))           