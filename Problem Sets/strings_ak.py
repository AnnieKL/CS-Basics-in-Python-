# Assume s is a string of lower case characters.
# Write a program that counts up the number of vowels contained in the string s. 
# Valid vowels are: 'a', 'e', 'i', 'o', and 'u'. 
# For example, if s = 'azcbobobegghakl', your program should print:

# Number of vowels: 5

count=0
for letter in s:
    if letter=="a" or letter=="e" or letter=="i" or letter=="o" or letter=="u":
            count+=1
print("Number of vowels: "+str(count))



# Assume s is a string of lower case characters.
# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print:

# Number of times bob occurs is: 2


count=0
index=0
for i in range(len(s)-2):
    if str(s[index]+s[index+1]+s[index+2])=="bob":
        count+=1
    index+=1
print("Number of times bob occurs is: "+str(count))



# Assume s is a string of lower case characters.
# Write a program that prints the longest substring of s in which the letters occur in 
# alphabetical order. 
# For example, if s = 'azcbobobegghakl', then your program should print: 

# Longest substring in alphabetical order is: beggh

# In the case of ties, print the first substring. For example, if s = 'abcbcd', 
# then your program should print:

# Longest substring in alphabetical order is: abc

str1_lngth=0
str2_lngth=0
diff=0

for i in range(len(s)-1):
    if s[i] <= s[i+1]:
        str1_lngth += 1
        if str1_lngth > str2_lngth:
            str2_lngth = str1_lngth
            diff = i + 1
    else:
        str1_lngth = 0
init_i = diff - str2_lngth
print('Longest substring in alphabetical order is:', s[init_i:diff+1])