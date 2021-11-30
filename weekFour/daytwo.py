arr = []

num = int(input('How many numbers we want to enter?:'))
print('Enter Values: ')

for k in range(num):
    arr.append(int(input()))


def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort(arr))