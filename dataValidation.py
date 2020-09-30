#ask for student's grades, attendance & # days of class.
# get GRADE 1 ---- DATA VALIDATION
data_valid = False
while (data_valid == False):    
    grade1 = float( input('What is the grade on the first test? '))
    if grade1 < 0 or grade1 > 10:
        print('Grade should be between 0 and 10.')
        continue
    else:
        data_valid = True

# get GRADE 2 ---- DATA VALIDATION
data_valid = False
while (data_valid == False):    
    grade2 = float( input('What is the grade on the second test? '))
    if grade2 < 0 or grade2 > 10:
        print('Grade should be between 0 and 10.')
        continue
    else:
        data_valid = True

absences = float( input('What is the number of absences? '))

# get ATTENDANCE DATA ---- DATA VALIDATION
data_valid = False
while (data_valid == False):    
    total_classes = float( input('What is the total number of classes? '))
    if total_classes < 0 or total_classes > 10:
        print('Grade should be between 0 and 10.')
        continue
    else:
        data_valid = True



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