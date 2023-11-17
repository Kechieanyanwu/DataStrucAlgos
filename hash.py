book = dict()

book["rice"] = 1.3
book["beans"] = 4.5

print(book["beans"])
print(book)

# shortcut

phonebook = {}
phonebook["Mummy"] = "0802222"
phonebook["Bro1"] = 99000
phonebook["Bro2"] = 93093402
phonebook["Emergency"] = 911

print(phonebook.get("Nkechi"))

print(phonebook)

voted = {}
def check_voter(name):
    if voted.get(name):
        print("Leave, rigger!")
    else:
        voted[name] = True
        print("Let them vote!")

check_voter("Nkechi")
check_voter("Nkechi")
check_voter("Chichi")

cached_links = {}
cached_links["homepage"] = "hostname/home"
cached_links["aboutpage"] = "hostname/aboutpage"

def serve_cached_pages(link):
    if cached_links.get(link): #if the link exists
        print("Serving cached pages of", cached_links[link]) #return cached data
    else:
        print("Making the server fetch the pages...")


serve_cached_pages("homepage")
serve_cached_pages("profile")