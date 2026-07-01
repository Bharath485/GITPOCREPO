# How to implement rotation?
# Here we consider right rotation for consistency, the left rotation can also be implemented using the same algorithms.

# Input: arr[] = {1, 2, 3, 4, 5, 6}, d = 2
# Output: {5, 6, 1, 2, 3, 4}
# Explanation: After first right rotation, arr[] becomes {6, 1, 2, 3, 4, 5} and after the second rotation, arr[] becomes {5, 6, 1, 2, 3, 4}

# Input: arr[] = {1, 2, 3}, d = 4
# Output: {3, 1, 2}
# Explanation: The array is rotated as follows:

# After first right rotation, arr[] = {3, 1, 2}
# After second right rotation, arr[] = {2, 3, 1}
# After third right rotation, arr[] = {1, 2, 3}
# After fourth right rotation, arr[] = {3, 1, 2}

# Python Program to right rotate the array by d positions
# by rotating one element at a time

# Function to right rotate array by d positions

arr = [1,2,3,4,5,6]
d = 2
n = len(arr)
def arryRotation(arr,d):
    for _ in range(d):
        last = arr[n-1]

        for i in range(n-1,0,-1):
            arr[i] = arr[i-1]
        arr[0] = last

if __name__ ==  "__main__":
    arr = [1,2,3,4,5,6]
    d = 2
    arryRotation(arr,d)
    for i in range(len(arr)):
        print(arr[i],end=" ")



