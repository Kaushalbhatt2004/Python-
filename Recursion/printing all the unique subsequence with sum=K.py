def find(idx, arr, subse, sum_, n, k, result):
    if idx == n:
        if sum_ == k:
            # Convert the subsequence to a tuple and add to the set for uniqueness
            result.add(tuple(subse))
        return
    
    # Include the current element in the subsequence
    subse.append(arr[idx])
    sum_ += arr[idx]
    find(idx + 1, arr, subse, sum_, n, k, result)

    # Exclude the current element from the subsequence
    subse.pop()
    sum_ -= arr[idx]
    find(idx + 1, arr, subse, sum_, n, k, result)

# Input handling
arr = []
n = int(input("Enter the size of the list: "))
print('Enter the numbers:')
for i in range(n):
    ele = int(input())
    arr.append(ele)

k = int(input("Enter the sum for which you want to calculate: "))
result = set()  # To store unique subsequences
subse = []  
find(0, arr, subse, 0, n, k, result)

# Print all unique subsequences
for subseq in result:
    print(list(subseq))



#We convert the list into a tuple before storing it in a set because in Python, lists are mutable (i.e., their contents can be changed), and mutable objects cannot be stored in sets. 
#Sets require their elements to be hashable, which means the elements must have a fixed hash value that doesn't change over time.