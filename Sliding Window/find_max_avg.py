from typing import List

def findmaxavg(nums:List[int],k:int)->float:
   i=0
   j=0
   sum=0
   n=len(nums)
   max_avg= float('-inf')

   while j<n:
      sum+=nums[j]

      if j-i+1 >= k:
         
         # Check if we have reached or exceeded the window size 'k'
         current_avg=sum/k
         max_avg=max(current_avg,max_avg)

         # Subtract the element that's sliding out of the window
         sum-=nums[i]
         i+=1

      j+=1

   return max_avg


# Example usage

nums=[1,12,-5,-6,50,3]
k=4
print(findmaxavg(nums,k))
