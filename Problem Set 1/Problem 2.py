# Assume s is a string of lower case characters.

# Write a program that prints the number of times the string 'bob' occurs in s. 
# For example, if s = 'azcbobobegghakl', then your program should print

# Number of times bob occurs is: 2



res=[]

for i in range(0,len(s)):
    res.append(s[i:i+3])
print("Number of times bob occurs is: "+str(res.count("bob")))    