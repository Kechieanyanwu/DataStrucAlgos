def is_happy_number(num):
    if num == 1:
        return True
    else:
    #initialise pointers to start with 
        slow = num
        fast = sum_of_squared_digits(num)
        print(slow, fast)  
        while slow != fast:
            if fast == 1: #if we have hit a happy number
                return True
            else: #keep advancing 
                slow = sum_of_squared_digits(slow)
                fast = sum_of_squared_digits(sum_of_squared_digits(fast))
                print(slow, fast)
        return False
    
    #can be changed to if slow not = fast and slow != 1






def sum_of_squared_digits(num): #helper function for is_happy_number

    total_sum = 0
    #repeatedly remove the last digit and add its square to the total
    while num > 0:
       # digit = num % 10
        #num = num // 10
        num, digit = divmod(num, 10)
        total_sum += digit ** 2
    return total_sum


# print(is_happy_number(19))
# print(is_happy_number(4))

# --------- Linked List cycle -----------

def detect_cycle(head):
    # might need to implement changing an array into a linkedlist, but later 
    if head is None:
        return False
    
    slow, fast = head, head

    while fast and fast.next: #continue looping through while you haven't reached the end of the list
        slow = slow.next
        fast = fast.next.next
        # if slow.data == fast.data:
        if slow == fast:
            return True
    return False


def get_middle_node(head):
    if head.next is None:
        return head
    slow, fast = head, head
    while fast and fast.next:
        slow = slow.next
        fast = fast.next.next
    return slow