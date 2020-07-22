blog_posts = ['fake news 1','' , 'fake news 2','' , 'fake news 3']

for post in blog_posts:
    if post == "": #skips empty strings
        continue
    else:
        print(post)

print('----------------------------')
myString = 'This is a string'
for char in myString:
    print(char)

print('----------------------------')
for x in range(0,10):
    print(x)

print('----------------------------')
person = {'first_name': 'Ben', 'last_name': 'Calvert', 'DOB': '1991', 'birth place': 'USA'}

for key in person:
    print(key, ':', person[key])

print('----------------------------')
blog_posts = {'news':['fake news 1','fake news 2', 'fake news 3'], 'sports': ['coronavirus, no sports']}

for category in blog_posts:
    print('Posts about', category)
    for post in blog_posts[category]:
        print(post)


