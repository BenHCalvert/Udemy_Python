# create dictionary for a person
person = {'name': 'Ben', 'gender': 'human', 'age': '29', 'address': 'Boise, ID', 'phone': '208.452.0475'}

print ('This program will give you information about Ben.')

uinput = input('What would you like to know about Ben?')

print(person.get(uinput, 'Sorry, Ben does not have that quality'))