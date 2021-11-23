#1. Create a list called cars and using a for loop print out items in the list.

cars = ["mercedes", "ford", "toyota", "hyundai", "subaru", "kia","volkswagen"]

for i in cars:
    print(i) 

#2. print firts 3 items in the list
print (cars[:3])

# 3. Create a function using the if statement 
if cars[0] == 'mercedes':
    print ("You own a mercedes!")

# 4. sort the list of cars
cars.sort()
print(cars)

#5.for loop printing odd numbers in range 20
for i in range(1,20,2):
    print (i)

#6. elif
a = 200
b = 33
if b > a:
  print("b is greater than a")
elif a == b:
  print("a and b are equal")
else:
  print("a is greater than b")

# 7. Create a variable that changes a name from lower case to upper case letters
myName = "kesa"
print (myName.upper())