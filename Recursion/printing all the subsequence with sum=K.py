def find(idx, arr, subse, sum_, n, k):
    if idx == n:
        if sum_ == k:
            # Print the subsequence as a list
            print(subse)
        return  # Return to prevent further recursion
    
    # Include the current element in the subsequence
    subse.append(arr[idx])
    sum_ += arr[idx]
    find(idx + 1, arr, subse, sum_, n, k)

    # Exclude the current element from the subsequence
    subse.pop()
    sum_ -= arr[idx]
    find(idx + 1, arr, subse, sum_, n, k)

# Input handling
arr = []
n = int(input("Enter the size of the list: "))
print('Enter the numbers:')
for i in range(n):
    ele = int(input())
    arr.append(ele)

k = int(input("Enter the sum for which you want to calculate: "))
subse = []  
find(0, arr, subse, 0, n, k)
