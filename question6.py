# Problem 6: Find a Number in a List


def find_number(numbers, target):
    for i, num in enumerate(numbers):
        if num == target:
            return i
    return -1

# numbers = [10, 25, 30, 45]
# target = 30
# numbers = [5, 8, 5, 9]
# target = 5
numbers = [10, 20, 30]
target = 99
print(find_number(numbers, target))



