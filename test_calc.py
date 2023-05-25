student_number = int(input('Enter number of students here: '))
student_tests = int(input('Enter number of tests: '))
sum_avg = 0.0
count = 0
while count <= student_number:
    total = 0.0
    count+=1
    print(f'Student {count} information:')
    id = int(input('Enter student ID: '))
    name = input('Enter student name: ')
    for tests in range (student_tests):
        score = int(input(f'Enter test score # {tests+1}:'))
        total += score
        avg = total/student_tests
    print('----------------------------------')
    print(f'-Student name:{name} \n-Average: {avg}')
    print('----------------------------------')
    sum_avg+=avg
print('Class average is:', sum_avg/student_number)
