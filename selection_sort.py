# selection sort in ascending order

arr = [6,1,5,2,3,9,3]

min = 0

for pos in range(len(arr)-1):
    min = pos
    for i in range(pos+1, len(arr)):
        if arr[i]< arr[min]:
            min = i
    arr[min], arr[pos] = arr[pos], arr[min]

print(arr)


# selection sort in decending order

arr = [6,1,5,2,3,9,3]

max = 0

for pos in range(len(arr)-1):
    max = pos
    for i in range(pos+1, len(arr)):
        if arr[i]> arr[max]:
            max = i
    arr[max], arr[pos] = arr[pos], arr[max]

print(arr)

