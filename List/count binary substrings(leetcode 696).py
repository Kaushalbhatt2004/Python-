class solution:

    def count_binary_strings(self,arr):
        prev=0
        sum=0
        curr=1

        for i in range(1,len(arr)):

            if arr[i]==arr[i-1]:
                curr+=1
            
            else:
                sum+=min(prev,curr)
                prev=curr
                curr=1
        
        sum+=min(prev,curr)
        return sum


sol=solution()
arr=[]
n=int(input("Enter the number of elements"))

for i in range(0,n):
    ele=int(input())
    arr.append(ele)

print(sol.count_binary_strings(arr))
