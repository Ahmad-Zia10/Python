def get_book():
    yield "The Power of Subconscious Mind"
    yield "Sapiens"
    yield "Mein Kampf"

stall = get_book() 
print(stall)# <generator object get_book at 0x00000257495653C0>. i.e. get_book generator function returns an iterable generator object

for book in stall:
    print(book)

def books():
    return ["The Laws of Power", "Emotional Intelligence", "Leo Tolstoy : Short stories"]

print(books())

def authors():
    yield "Joseph Murphy"
    yield "Charles Dawin"
    yield "Leo Tolstoy"

print(next(authors()))
print(next(authors()))
print(next(authors())) # All three give same value ,"Joseph Murphy" because everytime I am calling authors() function, which each time generates a new generator object, wihch starts from first yield.

authors = authors() #After this assignment authors no longer refers to the function — it refers to the generator object. The function object still exists somewhere in memory until garbage-collected, but you’ve lost the name reference to it.
print(next(authors))
print(next(authors))

print(f"Id of authors vairable reference to generator object : {id(authors)}")

# temp = authors() # Error : 'generator' object is not callable
# print(temp)