# bubble sort

arr = [1,6,5,2,3,9,3]

a = False

while not a:
    a = True
    for i in range(len(arr)-1):
        if arr[i] > arr[i+1]:
            a = False
            # temp = arr[i]
            # arr[i] = arr[i+1]
            # arr[i+1] = temp
            arr[i] , arr[i+1] = arr[i+1], arr[i]

print(arr)