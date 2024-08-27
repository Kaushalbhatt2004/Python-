
def isAnagram(s: str, t: str) -> bool:
    
    # Preprocess the strings: remove non-letter characters and convert to lowercase
    s = ''.join(filter(str.isalpha, s)).lower()
    t = ''.join(filter(str.isalpha, t)).lower()
    
    # If lengths differ, they cannot be anagrams
    if len(s) != len(t):
        return False
    
    # Create frequency counters for both strings
    count = [0] * 26  # Assuming only lowercase English letters
    
    # Increment count for characters in s
    for char in s:
        count[ord(char) - ord('a')] += 1
    
    # Decrement count for characters in t
    for char in t:
        count[ord(char) - ord('a')] -= 1
    
    # Check if all counts are zero
    return all(x == 0 for x in count)

# Test the function
s = 'cat is car'
t = 'car is cat'
print(isAnagram(s, t))  # Expected output: True




# filter(str.isalpha, t):

#filter() is a built-in function that applies a function to each element of an iterable (in this case, t) and returns an iterator that only includes elements for which the function returns True.
#str.isalpha is a method that returns True if a character is an alphabetical letter (i.e., a to z or A to Z) and False otherwise.
#So, filter(str.isalpha, t) filters out any characters from t that are not alphabetical. It effectively removes spaces, punctuation, digits, and any other non-alphabetical characters.

# ''.join(...):

#''.join() takes an iterable of strings and concatenates them into a single string. The '' (empty string) is the separator, meaning there is no space or character between the concatenated elements.
#This part of the code joins the filtered alphabetical characters into a single string, effectively removing all non-alphabetical characters from t.
#.lower():

# .lower() is a string method that converts all characters in the string to lowercase.
#This ensures that the comparison is case-insensitive, so A and a are treated as the same character.




# ord(char):

# ord() is a built-in Python function that returns the Unicode code point (integer) of a given character. For example, ord('a') returns 97, and ord('b') returns 98.

# all() Function:

# all() is a built-in Python function that takes an iterable (like a list or generator) and returns True if all elements of the iterable are true. If any element is false, it returns False.
# In this context, all() is used to check if every element in the iterable meets a specific condition.