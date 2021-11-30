# arr = []

# num = int(input('How many numbers we want to enter?:'))
# print('Enter Values: ')

# for k in range(num):
#     arr.append(int(input()))


# def bubblesort(array):
#     n = len(array)
#     for i in range(n):
#         for j in range(n-i-1):
#             if array[j] > array[j+1]:
#                 array[j], array[j+1] = array[j+1], array[j]
#     return array


# print(bubblesort(arr))


arr1 = [100, 49, 3,22,67,29]

def selectionsort(array):
    n= len(array)
    for i in range(n):
        cur_index = i
        for j in range(i+1, n):
            if array[cur_index] > array[j]:
                cur_index = j
        array[i], array[cur_index] = array[cur_index], array[i]
    return array


print(selectionsort(arr1))