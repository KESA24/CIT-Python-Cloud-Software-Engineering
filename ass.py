# Create a whileLoop that prints out "I have 1-10 grapes in my hand"
print("---------------------GRAPES-------------------------------")
grapes = 0
while grapes <= 10:
    grapes += 1
    print("I have " + str(grapes) + " grapes in my hand")

print("-------------------ODD NUMBERS---------------------------------")
# Create a whileLoop that only prints odd numbers upto 19
odd_numbers = 0
while odd_numbers <= 19:
    odd_numbers += 1
    if odd_numbers % 2 != 0:
        print(odd_numbers)

print("--------------------NESTED DICTIONARY--------------------------------")

# Create a nested dictionary that prints heathy foods- vegetables and fruits
healthy_foods = {

    'Vegetables': {
        'Green': 'Kales',
        'BabyGreen': 'Spinach',
        'White': 'Cucumbers',
        'Orange': 'Carrots',
        'Purple': 'Onions',
    },

    'Fruits': {
        'Sour': 'Oranges',
        'Sweet': 'Mangoes',
        'Sugary': "Pineapples",
        'Watery': 'Watermelon',
        'SourSweet': 'Tangerine',
        'Bittersweet': 'Tamarinds'
    }
}
print(healthy_foods)

print("-------------------------------------------------------")

for  food_type, food_examples in healthy_foods.items():
    for food_type in food_examples:
        print(food_examples[food_type] ,  "are" , food_type )



print("-----------------------EVEN NUMBERS-----------------------------")

# Create a function that prints only even numbers to 20
def even_numbers():
    even_number = 0
    while even_number <= 20:
        even_number += 1
        if even_number % 2 == 0:
            print(even_number)

even_numbers()


