# Using the bubllesort method, create another way to sort an unsorted list
# introducing swapped variable to prevent redudancy
print('--------------------------------------------Bubblesort---------------------------------------------------')
def bubbleSort(array):
  for i in range(len(array)):
    swapped = False
    for j in range(0, len(array) - i - 1):
      if array[j] > array[j + 1]:
        temp = array[j]
        array[j] = array[j+1]
        array[j+1] = temp
        swapped = True
    if not swapped:
      break
  return array

data = [-2, 45, 0, 11, -9]
print(bubbleSort(data))


# Usinng the selection sort method, create another way to sort an unsorted list
print('------------------------------------------------selectionsort---------------------------------------------------')

def selectionSort(array, size):
   
    for step in range(size):
        min_idx = step

        for i in range(step + 1, size):
         
            # to sort in descending order, change > to < in this line
            # select the minimum element in each loop
            if array[i] < array[min_idx]:
                min_idx = i
         
        # put min at the correct position
        (array[step], array[min_idx]) = (array[min_idx], array[step])


data = [-2, 45, 0, 11, -9]
size = len(data)
selectionSort(data, size)
print(data)

# # create a nesting loop that prints two lists. colors and cars
print('-----------------------------------------nested loop---------------------------------------------------')
def car_colors():
    colors=['red', 'yellow','green', 'mustard', 'cream']
    cars = [ 'bugatti', 'limousine', 'rangerover', 'mustang', 'raptor']

    for color in colors:
        for car in cars:
            print(car, color)

car_colors()