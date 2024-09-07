def isAnagram(s,t):
        # If lengths differ, they cannot be anagrams
        if len(s) != len(t):
            return False
        
        # Create frequency counters for both strings
        count = [0] * 26  # Assuming only lowercase English letters
        
        for c in s:
            count[ord(c) - ord('a')] += 1 #In Python, the ord() function is used to get the ASCII value of a character, which is used similarly to the c - 'a' logic in C++.
        
        for c in t:
            count[ord(c) - ord('a')] -= 1
        
        # Check if all counts are zero
        for i in count:
            if i != 0:
                return False
        
        return True

s=[]
t=[]
n=int(input("enter the size of s string"))
for i in range(0,n):
    ele=input()
    s.append(ele)

m=int(input("enter the size of string t"))
for i in range(0,m):
    ele=input()
    t.append(ele)

print(isAnagram(s,t))

