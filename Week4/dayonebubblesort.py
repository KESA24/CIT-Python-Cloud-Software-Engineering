
arr = [5,88,-1,-1,55,124,8,77,40,-20,4, -4]

def bubblesort(array):
    n = len(array)
    for i in range(n):
        for j in range(n-i-1):
            if array[j] > array[j+1]:
                array[j], array[j+1] = array[j+1], array[j]
    return array

print(bubblesort(arr))

