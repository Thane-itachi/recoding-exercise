# Problem 10: Move All Zeros to the End
# Description
# Write a function named move_zeros(numbers) that returns a list where all zeros have been moved to the end while keeping the other numbers in their original order.

# Hints
# First think about what should happen to the non-zero values.
# Keep track of how many zeros you encounter.
# After processing the numbers, how could you add the correct number of zeros?


def move_zeros(numbers):
    result = []
    zero_count = 0
    for num in numbers:
        if num != 0:
            result.append(num)
        else:
            zero_count += 1
    for _ in range(zero_count):
        result.append(0)
    return result

# numbers = [0, 1, 0, 3, 12]
# numbers = [1, 2, 3]
numbers = [0, 0, 5]
print(move_zeros(numbers))                   