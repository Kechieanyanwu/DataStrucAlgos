graph = {}

graph["you"] = ["claire", "bob", "alice"]
graph["claire"] = ["Thom", "johnny"]
graph["alice"] = ["peggy"]
graph["bob"] = ["anuj", "peggy"]
graph["anuj"] = []  
graph["peggy"] = []  
graph["johnny"] = []  
graph["thom"] = []  


#implementing breadth-first search algorithm

from collections import deque




def search(name):
    search_queue = deque() #creates a new queue
    search_queue += graph[name] #adds all your neighbours to the queue
    searched = []
    while search_queue:
        person = search_queue.popleft() #grabs the first person off the queue
        if not person in searched:
            if person_is_seller(person):
                print (person, "is a mango seller!")
                return True
            else: 
                search_queue += graph[person]
                searched.append(person)
    return False    


def person_is_seller(name):
    return name[-1] == "m"


# search("you")
print(search("bob"))