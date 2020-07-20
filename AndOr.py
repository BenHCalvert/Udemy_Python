#ask for student's grades, attendance & # days of class.
grade1 = float( input('What is the grade on the first test? '))
grade2 = float( input('What is the grade on the second test? '))
absences = float( input('What is the number of absences? '))
total_classes = float( input('What is the total number of classes? '))

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