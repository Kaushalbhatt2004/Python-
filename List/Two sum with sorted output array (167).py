
def two_sum (arr,target):
    sum=0
    i=0
    j=len(arr)-1

    while i<j:
        sum=arr[i]+arr[j]
        
        if sum>target:
            j-=1
        elif sum<target:
            i+=1
        else:
            return [i+1,j+1]
    


arr=[2,7,11,15]
target = 9
print(two_sum(arr,target))