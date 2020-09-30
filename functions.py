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

def addr(n1=0, n2=0, n3=0, n4=0, n5=0, n6=0, n7=0, n8=0, n9=0, n10=0):
    sum = n1 + n2 + n3 + n4 + n5 + n6 + n7 + n8 + n9 + n10
    print("The sum is: ", sum)
addr(1, 300, 200)
