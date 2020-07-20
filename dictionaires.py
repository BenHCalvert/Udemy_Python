# this is a list
person = ['Ben', 'Calvert', '1991', 'USA']

# this is a dictionary (object in JS)
dictionaryPerson = {'first_name': 'Ben', 'last_name': 'Calvert', 'DOB': '1991', 'birthPlace': 'USA'}

type(dictionaryPerson)

print(dictionaryPerson['last_name'])

# change DOB to 1990
dictionaryPerson['DOB'] = '1990'

# add a key value pair to the dictionary
dictionaryPerson['parents'] = ['Don', 'Lisa']

#add third parent
dictionaryPerson['parents'].append('Kristine')

# return the value of first_name else return the message
dictionaryPerson.get('first_name', 'first name does not exist.')
