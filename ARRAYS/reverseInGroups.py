arr = [1,2,3,4,5,6,7,8]
k = 6

def reverseInGroups(arr,k):
    arrLen = len(arr)
    sep = int(arrLen/k)
    left = arr[0:k][::-1]
    right = arr[len(left):k+k][::-1]
    if len(arr)%k == 0:
        print(True)
        rev = left + right
        
    if len(arr)%k != 0:
        print(True,'Line16')
        remaining = []
        Tmprev = left + right
        for i in range(len(arr)):
            if arr[i] not in Tmprev:
                remaining.append(arr[i])
        rev = left + right + remaining[::-1]
        
    return rev
sep = reverseInGroups(arr,k)
print(sep)
