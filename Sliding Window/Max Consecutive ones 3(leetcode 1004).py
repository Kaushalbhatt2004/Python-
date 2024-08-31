from typing import List

def func(nums,k):
    l=0
    r=0
    maxlen=0
    zeroes=0

    while r<len(nums):
        if nums[r]==0:
            zeroes+=1

        while zeroes>k:
            if nums[l]==0:
                zeroes-=1
            l+=1

        if(zeroes<=k):
            maxlen=max(maxlen,r-l+1)
        
        r+=1

    return maxlen




nums=[1,1,1,0,0,0,1,1,1,1,0]
k=2
print(func(nums,k))