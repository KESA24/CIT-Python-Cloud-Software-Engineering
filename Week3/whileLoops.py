x = 1
while x!= 10:
    print(x)
    break

i = 0
while i== 1:
    print(i)
    if i >= 5:
        print('Breaking')
print('Finish')

y = 1

while y <=5:
    print(y)
    y+=1
    if y ==2:
        print("Statement")
        continue

amount_of_money = 1

while amount_of_money != 10:
    amount_of_money+=1
    print("I received" +" " + "$" + str(amount_of_money))

b=1
while b < 10:
    if b%2 == 0:
        print(str(b)+ " is even")
    else:
        print(str(b)+ " is odd")
    b+=1