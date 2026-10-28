# Problem 4: Count Even Numbers

def count_even(numbers):
    count = 0
    for number in numbers:
        if number % 2 == 0:
            count = count + 1
    return count
# numbers = [1, 2, 3, 4, 6]
numbers = [1, 3, 5, 7]
print(count_even(numbers))    