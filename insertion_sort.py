#insertion sort

arr = [6,3,1,2,8,4,5]


for i in range(1, len(arr)):
    cur = arr[i]
    j = i-1
    while j>=0 and cur < arr[j]:
        arr[j+1] = arr[j]
        j-=1
    arr[j+1] = cur

print(arr)