# 3. Write a one-line piece of code, using the print () function, as well as the newline and escape characters, 
# to match the expected result outputted on three lines.
# Expected output:
#  "I'm" 
# ""learning"" 
# """Python"""

print ("\"I\'m\" \n \"\" learning \"\" \n \"\"\" python \"\"\" ")

# Write a program in python that finds the sum of two numbers using the concept of variables
z=7
t=8
numSum = (t+z)
print(numSum)

#Write a program in python that prints out the product of two numbers using the concept of input function.
print ('Enter the first number')
x = input ()
firstNum = int(x)
print ('Enter the second number')
y = input ()
secondNum = int(y)
print ('Your product is ', firstNum*secondNum)


# Write a python program that requests the user to input their name, two numbers X which is their birth year 
# and Y which is the current year. This program should print out the years of the user. i.e. (user is 12 years old)

x, y, z = input("Enter your name, birth year and the current year : ").split()
birthYear = int(y)
currentYear = int(z)
print (x , 'is', currentYear-birthYear, "years old")