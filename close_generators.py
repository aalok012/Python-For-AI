def mystery():
    print ("A")
    yield 1
    
    print("B")
    yield 2
    
    print ("C")
    yield 3

get = mystery()

print(next(get))
print(next(get))

for value in get:
    print(value)
    
get.close() # closes the generator gracefully