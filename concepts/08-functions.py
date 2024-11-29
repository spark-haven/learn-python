def greet(name):
    #print("Hello, " + name + "!")
    print(f"Hello, {name}!")

greet("Alice")

# Functions can return stuff

def find_num_chars(word):
    return len(word)

num_chars = find_num_chars("Alice")
print(num_chars)
