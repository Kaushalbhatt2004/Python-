#input=aabbbbeeeeffgggg
#output=a2b4e4f2g3
s = "aabbbbeeeeffgg"
result = ""
count = 1

if s:  # Check if the string is not empty
    for i in range(1, len(s)):
        if s[i] == s[i - 1]:
            count += 1
        else:
            result += s[i - 1] + str(count)  # Append the character first, then the count
            count = 1
    result += s[-1] + str(count)  # Append the last character and its count

print(result)
