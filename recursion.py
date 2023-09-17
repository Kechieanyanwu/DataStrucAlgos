# what's the need for a base case?
def infinite_countdown(i): # infinite_countdown(5) -- this should result in a Recursion error
    print(i)
    infinite_countdown(i - 1)

def countdown(i): # Has a base case that doesn't call the recursive function
    print(i)
    if i <= 1:
        return 
    countdown(i - 1)


# ooh, a Call stack!
def greet(name):
    print("hello, " + name + "!")
    greet2(name)
    print("getting ready to say bye...")
    bye()

def greet2(name):
    print("how are you, " + name + "?")

def bye():
    print("ok bye!")

# the call stack with recursion

def fact(x):
    if x == 1:
        return 1
    else:
        return x * fact(x - 1)
    

print(fact(4))