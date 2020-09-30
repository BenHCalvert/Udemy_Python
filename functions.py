# creating the function
def say_hello():
    print('hello')

# calling the function
say_hello()

# function that takes one argument
def say_hi_to_person(person):
    print("Hello " + person + ", how are you doing!?")

say_hi_to_person("Ben")
say_hi_to_person("Kristine")

# function to convert a given temp in F to C
def fahr2celcius(fahr):
    celsius = round(((5 * (fahr -32)) /9),2)
    return celsius

print (fahr2celcius(100))

# Set a default value for one of the function's arguments(parameters). Won't give an error if we only pass one argument when the function is called.
def hiThere(person1, person2="Ben"):
    print("Hello " + person1 + ", how are you doing!?")
hiThere("Johnny")
