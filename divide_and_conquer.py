# divide and conquer is a recursive technique used to solve problems
# if using D&C on a list, base case is probs empty array / array of one item 

import random

def sum(arr): #recursive sum array function
    if len(arr) == 0:
        return 0
    if len(arr) == 1:
        return arr[0]

    return arr[0] + sum(arr[1:])

# print(sum([1,2,4,5]))

def count_array_items(arr): #recursive function to count items in a list
    if arr == []:
        return 0
    else: 
        return 1 + count_array_items(arr[1:])

# print(count_array_items([3,4,5,6]))

def max_num_in_array(arr): #find maximum number in a list
    if len(arr) == 0 or len(arr) == 1:
        return
    if len(arr) == 2:
        return arr[0] if arr[0] > arr[1] else arr[1]
    sub_max = max_num_in_array(arr[1:])
    return arr[0] if arr[0] > sub_max else sub_max
    

# print(max_num_in_array([1,4,5,3,7,7,90,35]))


#Quick-sort uses D&C

def quicksort(array): 
    if len(array) < 2:
        return array
    else:
        random_index = random.randint(0, (len(array) - 1))
        print(random_index)
        pivot = array[random_index] #if implementing, choose a random element as a pivot, the average runtime becomes O(n log n)
        lower = [i for i in array if i < pivot]
        equal = [i for i in array if i == pivot]
        higher = [i for i in array if i > pivot]
        return quicksort(lower) + equal + quicksort(higher)
    

print(quicksort([10,5,3,45,2, 35,44,2,1,44,2]))
    

