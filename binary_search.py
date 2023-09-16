

def binary_search(sorted_array, item):
    low = 0
    high = len(sorted_array) - 1
    while low <= high:
        mid = (low + high) // 2
        guess = sorted_array[mid]
        if guess == item:
            return mid
        if guess < item:
            low = mid + 1
        else:
            high = mid - 1
    return None


my_list = [1,3,4,7,8,9]

print(binary_search(my_list, 9))
print(binary_search(my_list, 19))

import math

print(math.log2(128))
print(math.log2(128 * 2))
print(math.log2(1000000000))

