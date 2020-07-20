comp_age = float(30)
user_age = float(input('What is your age '))

if(comp_age > user_age):
    print(comp_age, 'is greater than', user_age, ' You are younger than the computer.')
elif(comp_age == user_age):
    print(comp_age, 'is equal to', user_age, ' You are the same age as the computer.')
else:
    print(comp_age, 'is less than', user_age, ' You are older than the computer.')