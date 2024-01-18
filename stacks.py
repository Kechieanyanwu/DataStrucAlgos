# reverse a string using a stack 

def reverse_string(string):
    # convert string into a char[]
    char_array = [char for char in string] # list comprehension. Super useful. Practice more of this when building w Python.l in JS would be string.split('')
    stack = [] # we will interact with the array as a stack, with only pushing and popping methods. Looking at the stack would involve checking out index -1
    for i in range(1, len(char_array) + 1): 
        stack.append(char_array[-i])
    reversed_string = ''.join(stack) # join elements of an array or list into a string 
    return reversed_string
#space complexity - O(n) because it grows proportional to the size of the input -  term is LINEARLY 
#time complexity - O(n) because it grows propotional to the size of the input 

# more concise implementation 
# def reverse_string(string):
#     stack = [char for char in string]
#     reversed_string = ''.join(stack[::-1])
#     return reversed_string

print(reverse_string('gnirts'));

# def reverse_string(string):
#     # stacks seem to relate to recursion. Perhaps because the structure of recursion is a stack itself? 
#     # convert string into a char[]
#     char_array = [char for char in string] # list comprehension. Super useful. Practice more of this when building w Python.l in JS would be string.split('')
#     stack = char_array # we will interact with the array as a stack, with only pushing and popping methods. Looking at the stack would involve checking out index -1

    
#     if len(stack) == 0: # the terminating factor of my recursion
#         return 
    
