class Solution:
    def generateParenthesis(self, n: int):
        ans = []
        self.find(ans, n, 0, 0, "")
        return ans

    def find(self, ans, n, o, c, current):
        if len(current) == 2 * n:
            ans.append(current)
            return
        if o < n:
            self.find(ans, n, o + 1, c, current + "(")
        if c < o:
            self.find(ans, n, o, c + 1, current + ")")

# Example usage
sol = Solution()
n = 3
print(sol.generateParenthesis(n))
