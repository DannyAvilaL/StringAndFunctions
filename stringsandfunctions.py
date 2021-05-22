"""
string = "Hello world"

print(type(string))

print(string)
print(f"How many l's : {string.count('l')}") # Returns the amount of characters found in the string

print(f"Where is the e: {string.find('e')}")

print(f"Where is the a: {string.find('a')}")

print(f"Where is the w: {string.index('w')}")           # W w

try:
    print(f"Where is the x: {string.index('x')}")
except:
    print("Your letter is not in the string")

number = -1 #int(input("Type a numer: "))

while number != -1:
    try:
        number = int(input("Type a number: "))
    except:
        print("I asked for a number not a word")

string = "This is a long string with different words and letters and number such as 1234213123"

listOfWords = string.split()

print(string)
print(f"List of string: {listOfWords}")

# Option no.1
for word in range(len(listOfWords)):
    print(listOfWords[word])

print("-------------------------")
# Option no.2 
for word in listOfWords:
    print(word)

print("Using iterators in the string")
print(string[::]) # [start: end: jump]

#print(string[:7:])

start = string.find("string")
end = string.find(" words")
print(string[start:end:])
"""



def function1():
    x = 10

print(type(function1))



def function2():

    def function3():
        print("inside of function 3")

        def function4():
            print("inside of function 4")

    return function3()

print(function2())
try:
    print(function3())
except:
    print("The function3 is local")









