print('This program has the user build a list of names and then prints one of the names at random.')

import random

names = []

while len(names) < 8:
    person = input('Type the name of a person: ')
    names.append(person)
print(names[random.randint(0,7)])


