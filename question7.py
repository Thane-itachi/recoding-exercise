# Problem 7: Reverse a List

def reverse_list(items):
    result = []
    i = len(items) - 1
    while i >= 0:
        result.append(items[i])
        i -= 1
    return result

# items = [1, 2, 3, 4]
items = ["a", "b", "c"]
print(reverse_list(items))
