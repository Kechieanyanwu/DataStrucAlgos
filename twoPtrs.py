# def is_palindrome(string):
#     #initialise two pointers at beginning and end
#     #traverse string and compare the values
#     start_ptr = s[0]
#     end_ptr = s[-1]

#     #while they arent in the middle:
#         if not start_ptr == end_ptr:
#             return False
#         else: 
#             start_ptr += 1
#             end_ptr -= 1
#     return True


def is_palindrome(s):
    left = 0
    right = len(s) - 1

    while left < right:
        if s[left] != s[right]:
            return False
        else:
            left += 1
            right -= 1
    
    return True


# print(is_palindrome("tart"))



def bubble_sort(arr):
    n = len(arr)

    # Traverse through all array elements
    for i in range(n):
        # Last i elements are already sorted, so we don't need to check them
        for j in range(0, n-i-1):
            # Swap if the element found is greater than the next element
            if arr[j] > arr[j+1]:
                arr[j], arr[j+1] = arr[j+1], arr[j]



def three_sum(nums, target):
    n = len(nums)
    nums.sort()
    for i in range(n - 2):
        left = i + 1
        right = n - 1
        while left < right:
            sum = nums[i] + nums[left] + nums[right]
            if sum == target:
                return True
            elif sum < target:
                left += 1
            else:
                right -= 1
    return False


# print(three_sum([-1, 2, 1, -4, 5, -3] , -8))

def remove_nth_last_node(head, n):
    counter = 0
    left = head
    right = head
    
    #begin to iterate
    while right.next:
        if counter >= n:
            left = left.next
        right = right.next
        counter += 1

    if left == head: 
        #checking to adapt for when its the head being removed
        head = left.next
        return head
    else:
        #assign the left node's next node to the skipped node
        left.next = (left.next).next
        return head

# alternative would be to just for i in range(n)
def remove_nth_last_node(head, n):
    left = head
    right = head
    
    #begin to iterate
    for i in range(n):
        right = right.next
    
    if not right:
        return head.next
    
    while right.next:
        left = left.next
        right = right.next
    
    left.next = left.next.next

    return head


def sort_colours(colours):
    n = len(colours)
    if n == 1:
        return colours
    red, white, blue = 0, 0, n - 1
    while white <= blue: 
        if colours[white] == 0:
            if colours[red] != 0:
                colours[white], colours[red] = colours[red], colours[white]
            red += 1
            white += 1
        elif colours[white] == 1:
            white += 1
        else: 
            if colours[blue] != 2:
                colours[white], colours[blue] = colours[blue], colours[white]      
                blue -= 1
    return colours




# print(sort_colours([2,0,2,1,1,0]))

import re #practice this again 
def reverse_sentence(sentence):
    # remove leading, trailing, and multiple spaces
    sentence = re.sub(" +", " ", sentence.strip())

    # convert the updated string to list of characters as strings are immutable in python
    sentence = list(sentence)
    str_len = len(sentence)

    str_rev(sentence, 0, str_len - 1)

    start = 0
    end = 0

    while start < str_len: 
        # using start < str_len because we have only finished a sentence when we move to the next one
        while end < str_len and sentence[end] != " ":
            end += 1
        str_rev(sentence, start, end - 1)
        start = end + 1
        end += 1
    return "".join(sentence)


def str_rev(sentence, start, end):
    while start < end:
        temp = sentence[start]
        sentence[start] = sentence[end]
        sentence[end] = temp
        
        start += 1
        end -= 1

# print(reverse_sentence("Hello I am a girl"))

def could_be_palindrome(s):
    #get length of palindrome
    n = len(s)
    #intialise pointer at beginning and end
    start = 0
    end = n - 1
    mismatch = 0
    #initialise mismatch counter 

    #while start < end 
    while start <= end:
        #compare start and end, if same, progress
        if s[start] == s[end]:
            start += 1
            end -= 1
        else:     #if not same, skip start and, check for palindrome
            mismatch += 1
            if is_palindrome(s[start+1:end+1]) or is_palindrome(s[start:end]):
                return True
            else: 
                return False
    return True



print(could_be_palindrome("abcdedadedecba"))
print(could_be_palindrome("madame"))