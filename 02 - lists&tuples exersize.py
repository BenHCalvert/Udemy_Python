# #1
months = ('January', 'February', 'March', 'April', 'May', 'June', 'July', 'August', 'September', 'October', 'November', 'December')

bday = input('Enter your birthday in the format "DD-MM-YYYY" ')

index = int(bday[3:5]) - 1
bd_month = months[index]

print('your birthday month is ', bd_month)

# #2
names = ['JimmyJoe', 'JimBob', 'BobbySue', 'BobOClock']
print("next we will add your name to a list of names")
yourname = input('What is your name? ')
names.append(yourname)
print('Here is the list of names with your name added', names)





