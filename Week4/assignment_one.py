# Create a tuple that grabs 2 items
print('------------------------------------------TUPLE----------------------------------------------------------------')
fruits =  ('oranges', 'mangoes','pineapples', 'watermelon', 'tamarind')
print (fruits[:2])

# # create a 6D list that prints six 6-D lists
print('------------------------------------------6DLIST--------------------------------------------------------------')
sixDlist = [
    [1,2,3,4,5,6],
    [7,8,9,10,11,17],
    [12,13,14,15,16,33],
    [18,19,29,30,31,32],
    [34,25,26,27,38,39],
    [40,41,42,43,44,45]
]
for i in range(6):
    print(sixDlist)

# # create a while loop that prints upto 20 but skips 15
print('--------------------------------------------------WHILELOOP---------------------------------------------------')
y = 0
while y <=19:
    y+=1
    if y ==15:
        print("Skipped 15")
        continue
    print(y)
# create a dictionary called phonebook that prints out names and phone number (nestingLoop is required)
print('-------------------------------------------------DICTIONARY------------------------------------------------')
phoneBook = {
    'Regina:': '0708910010',
    'Ronald:': '045677189'

}
for i,j in phoneBook.items():
    print(i,j)