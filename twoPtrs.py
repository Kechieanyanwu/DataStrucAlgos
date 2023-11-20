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


print(three_sum([-1, 2, 1, -4, 5, -3] , -8))