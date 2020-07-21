#ask for user's height and weight. 
uHeight = float( input('What is your heigh in inches? '))
uWeight = float( input('What is yout weight in pounds? '))


# calc BMI
bmi = (uWeight / (uHeight * uHeight)) * 703

# print user's BMI
print('Your BMI is: ', round(bmi , 1))


# logic tests to determine BMI classification. Both statements with AND must be true for the boolean to return true. if you use OR only one must be true for the test to return TRUE.
if (bmi > 18.5):
    print("Your BMI classification is 'underweight' ")
elif (bmi > 18.5 and <= 24.9):
    print("Your BMI classification is 'normal' ")
elif (bmi > 24.9 and <= 29.9):
    print("Your BMI classification is 'overweight' ")
else:
    print("Your BMI classification is 'obese' ")