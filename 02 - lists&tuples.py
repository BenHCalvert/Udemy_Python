# this is a string
studentString = 'john, mary, steve'

# this is a list aka array, they are a sequence
students = ['john', 'mary', 'steve']
print(type(students))
print(len(students))

print(students[-1])
print(students[:2])



# tuples are like lists except they are immutable

months = ('January', 'February', 'March')
print(type(months))

# change an element in the list
students[0] = 'Ben'
print(students)

# add an element to the list
students.append('Kristine')
print(students)

students.insert(0, 'Edgar')
print(students)


students2 = ['paul', 'james']
students + students2

