#Create a dictionary called "Report Card", the keys will be the name of the students and the values will be their grades
print('-------------------------report_card-----------------------')
report_card = {
    "Patricia": 95,
    "Shona": 90,
    "Charity": 85,
    "Gloria": 93,
    "Elizabeth": 88
}

print (report_card)

#In your report card dictionary change one of the students grades
print('-----------------------marks_change for charity-----------------------')

report_card['Charity'] = 98
print(report_card)

#Create a while loop that prints 10 numbers but it skips the number 3

print('------------------------skipping while loop-----------------------')

numero_uno = 0

while (numero_uno <= 9):
    numero_uno += 1
    if numero_uno == 3:
        print('skipped 3')
        continue
    print(numero_uno)

# Create a list that prints out all the items outside the list
print('------------------------print list items outside-----------------------')
student_marks = [83, 84,88, 93, 97, 86]
for i in student_marks:
    print(i)

# Create a if statement that uses the input method.
print('----------------------if statement with input method----------------------')

username = input('Provide your username: ')
if username.lower() == "kesapr":
    print('Welcome to NASA')
else:
    print('Wrong username')

usermusk = input('Provide your username: ')
if usermusk.upper() == "ELON MUSK":
    print('Welcome to SpaceX')
else:
    print('Unauthorised user')