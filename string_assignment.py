
# Explain the difference between immutable and mutable types in Python. How does this apply to strings?
In Python, mutable and immutable refer to whether an object’s value can be changed after it's created. Mutable types can be modified in place, meaning their content can be changed without creating a new object. Examples of this include lists, dictionaries, and sets. On the other hand, immutable types cannot be changed after they are created. Any operation that tries to alter them will actually result in the creation of a new object with the modified value. Examples of immutable types include integers, floats, tuples, and strings.
This concept directly applies to strings in Python. Since strings are immutable, you cannot change a single character in a string once it's created. If you try to modify a string, Python creates an entirely new string object with the change, rather than altering the original string. This behavior is important to understand when you're manipulating text, as it can impact performance and how you manage memory in your programs.

#Describe the role of escape characters in Python strings. Give examples.
Escape characters in Python are used to represent characters that are difficult or impossible to type directly into a string, such as newlines, tabs, or quotes. They start with a backslash (\), which tells Python to treat the next character in a special way rather than as a literal character.
For example, if you want to include a double quote inside a string that's enclosed in double quotes, you use the escape character \" to prevent Python from ending the string too early. Similarly, \n represents a newline, causing the text to move to the next line when printed, and \t represents a tab space.

#Write a Python program that takes a string and removes all vowels.

str1="Write a Python program that takes a string and removes all vowels."
result = ""
for char in str1:
    if char not in "aeiou":
        result += char
print(result)



#Given a string, write a program to count the frequency of each character.
frequency1={}
str1="Given a string, write a program to count the frequency of each character."

for char in str1:
    if char in frequency1:
        frequency1[char] +=1
    else:
        frequency1[char] = 1
        
for key,value in frequency1.items():
    print(f"'{key}': '{value}")



#Write a Python program to check if two given strings are anagrams of each other
frequency1={}
frequency2={}
str1="listen"
str2="silent"

for char in str1:
    if char in frequency1:
        frequency1[char] +=1
    else:
        frequency1[char] = 1
        
for char in str2:
    if char in frequency2:
        frequency2[char] +=1
    else:
        frequency2[char] = 1
        
if (frequency1 == frequency2):
    print("They are anagrams")
else:
    print("They are not Anagrams")


#Write code to reverse the order of words in a sentence, without using built-in reverse functions
lst1 = "Write code to reverse the order of words in a sentence, without using built-in reverse functions"
lst2 = lst1.split(" ")[::-1]
print(lst2)


#Write a Python program to find the longest substring without repeating characters.
def longest_unique_substring(s):
    seen = {}
    start = 0
    max_len = 0
    longest = ""

    for i, char in enumerate(s):
        if char in seen and seen[char] >= start:
            start = seen[char] + 1 

        seen[char] = i  
        current_len = i - start + 1

        if current_len > max_len:
            max_len = current_len
            longest = s[start:i+1]

    return longest

#Write a program to check if a string is a palindrome, ignoring spaces and punctuation,
def is_palindrome(s):
    
    cleaned=""
    for char in s:
        if char.isalnum():
            cleaned+=char.lower()
            
    if cleaned == cleaned[::-1]:
        print("Its a palindrome")
    else:
        print("Its not a palindrome")

#Write code to convert a string so that the first letter of each word is capitalized (like title case), without using .
#with out using Title()

str1="my name is siddhant girdhar and i love ust"
words=str1.split()
result=""

for word in words:
    result+= word[0].upper() + word[1:] + " "
    
print(result)
