def is_palindrome(s):
    left = 0
    right = len(s) - 1
    s = s.lower()
    

    while left <= right:
        if not s[left] == s[right]:
            return False
        else: 
            left += 1
            right -= 1
    return True


print(is_palindrome("Racecar"));
print(is_palindrome("Raceacar"));