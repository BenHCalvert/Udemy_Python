#ask for student's grades, attendance & # days of class.
# get GRADE 1 ---- DATA VALIDATION
data_valid = False
while (data_valid == False):    
    grade1 = input("What is the grade on the first test? ")
    try:
        grade1 = float(grade1)
        if grade1 < 0 or grade1 > 10:
            print("Grade should be between 0 and 10.")
            continue
        else:
            data_valid = True
    except:
        print("please enter a numerical value.")

# get GRADE 2 ---- DATA VALIDATION
data_valid = False
while (data_valid == False):    
    grade2 = input("What is the grade on the second test? ")
    try:
        grade2 = float(grade2)
        if grade2 < 0 or grade2 > 10:
            print("Grade should be between 0 and 10.")
            continue
        else:
            data_valid = True
    except:
        print("please enter a numerical value.")

# get total number of classes
data_valid = False
while (data_valid == False):    
    total_classes = input("What is the total number of classes? ")
    try:
        total_classes = float(total_classes)
        if total_classes <= 0:
            print("Total classes must be greater than 0.")
            continue
        else:
            data_valid = True
    except:
        print("please enter a numerical value.")

# get # of absences and check that value is numberical.
data_valid = False
while (data_valid == False):
    absences = input('What is the number of absences? ')
    try:
        absences = float(absences)
        if absences > total_classes:
            print ("The number of absences cannot be greater than the number of classes")
        else:
            data_valid = True
    except:
        print("Please enter a numerical value.")
    
# calc grade and attendance rate
avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

# print overall grade and att. rate
print('Average grade: ', round(avg_grade,2))
print('Attendance rate: ', str(round((attendance * 100),2))+'%')

# logic tests to determine if student passed. Both statements with AND must be true for the boolean to return true. if you use OR only one must be true for the test to return TRUE.
if (avg_grade >= 6 and attendance >= 0.8):
    print('The student has passed')
elif (avg_grade < 6 and attendance < 0.8):
    print('The student has failed due to an average grade lower than 6 and an attendance rate lower than 80%')
elif (attendance >= 0.8):
    print('The student has failed due to an average grade lower than 6.0.')
else:
    print('The student has failed due to an attendance rate lower than 80%.')