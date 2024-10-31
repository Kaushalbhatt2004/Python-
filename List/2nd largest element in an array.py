def large(arr):

    max = arr[0]
    
    max2 = float('-inf')  # Initialize max2 to the smallest possible value just in case the value is negative it might be overlooked because we've intialised the variable with 0

    for i in range(1, len(arr)):
        if arr[i] > max:
            max2 = max
            max = arr[i]
        elif arr[i] > max2 and arr[i] != max:
            max2 = arr[i]

    return max2


arr = [1, 2, 4, 5, 34, 2, 4, 24, 23, 11, 30]
print(large(arr))
