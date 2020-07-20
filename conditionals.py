#ask for student's grades, attendance & # days of class.
grade1 = float( input('What is the grade on the first test? '))
grade2 = float( input('What is the grade on the second test? '))
absences = float( input('What is the number of absences? '))
total_classes = float( input('What is the total number of classes? '))

# calc grade and attendance rate
avg_grade = (grade1 + grade2) / 2
attendance = (total_classes - absences) / total_classes

print('Average grade: ', round(avg_grade,2))
print('Attendance rate: ', str(round((attendance * 100),2))+'%')

if (avg_grade >= 6):
    if(attendance >= 0.8):
        print('The student has passed')
    else:
        print('The student has failed due to an attendance rate lower than 80%.')
elif (attendance >= 0.8):
    print('The student has failed due to an average grade lower than 80%.')
else:
    print('The student has failed due to an average grade lower than 6 and an attendance rate lower than 80%')