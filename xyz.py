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
        
if (key, value in frequency1.items() == frequency2.items()):
    print("They are anagrams")
else:
    print("They are not")