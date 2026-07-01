arr = [12, 35, 1, 10, 34, 1]
def secoundThirdLargest(arr):
    arr.sort()
    
    largest = -1
    secoundLargest = -1
    thirdLargest = -1
    for i in range(len(arr)):
        if arr[i] > largest:
            largest = arr[i]
            
    for i in range(len(arr)):
        if arr[i] > secoundLargest and arr[i] != largest:
            secoundLargest = arr[i]
    
    for i in range(len(arr)):
        if arr[i] > thirdLargest and arr[i]!= secoundLargest and arr[i] != largest:
            thirdLargest = arr[i]

    return thirdLargest # change the return statement based on the requirement.
    
a = secoundThirdLargest(arr)
print(a)