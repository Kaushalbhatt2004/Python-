from typing import List

class Solution:
    def find(self, idx: int, arr: List[int], target: int, ans: List[List[int]], ds: List[int]) -> None:
        if idx == len(arr):
            if target == 0:
                ans.append(ds.copy())  # Add a copy of the current combination to the results
            return
        
        if arr[idx] <= target:
            ds.append(arr[idx])
            self.find(idx, arr, target - arr[idx], ans, ds)  # Don't increment idx to allow reuse
            ds.pop()  # Backtrack to explore other combinations
        
        self.find(idx + 1, arr, target, ans, ds)  # Increment idx to move to the next element
    
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ans = []
        ds = []
        self.find(0, candidates, target, ans, ds)
        return ans

# Example usage:
sol = Solution()
candidates = [2, 3, 6, 7]
target = 7
print(sol.combinationSum(candidates, target))  # Output: [[2, 2, 3], [7]]
