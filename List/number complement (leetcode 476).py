class Solution:
    def findComplement(self, num: int) -> int:
        # List to store the binary representation
        ans = []
        sum = 0
        
        # Convert the number to binary (reversed order)
        while num > 0:
            ans.append(num % 2)
            num = num // 2
        
        # Calculate the complement
        for i in range(len(ans)):
            if ans[i] == 0:
                sum += (1 << i)  # Equivalent to 2^i
        
        return sum

# Example usage
sol = Solution()
num = 5
print("Complement of", num, "is:", sol.findComplement(num))
